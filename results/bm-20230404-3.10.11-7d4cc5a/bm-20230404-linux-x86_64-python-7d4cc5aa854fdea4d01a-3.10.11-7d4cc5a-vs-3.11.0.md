
# Results vs. 3.11.0

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: linux-x86_64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.24x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 335 ms: 1.29x slower                                                 |
| chameleon      | 6.47 ms                                                | 8.93 ms: 1.38x slower                                                |
| docutils       | 2.63 sec                                               | 3.21 sec: 1.22x slower                                               |
| html5lib       | 64.5 ms                                                | 85.4 ms: 1.32x slower                                                |
| tornado_http   | 96.3 ms                                                | 131 ms: 1.36x slower                                                 |
| Geometric mean | (ref)                                                  | 1.31x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                 |
| float          | 77.2 ms                                                | 108 ms: 1.40x slower                                                 |
| nbody          | 93.1 ms                                                | 137 ms: 1.48x slower                                                 |
| Geometric mean | (ref)                                                  | 1.25x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                |
| regex_dna      | 204 ms                                                 | 213 ms: 1.05x slower                                                 |
| regex_v8       | 22.0 ms                                                | 25.5 ms: 1.16x slower                                                |
| regex_compile  | 138 ms                                                 | 176 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_list        | 4.91 us                                                | 4.80 us: 1.02x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 163 ms: 1.03x slower                                                 |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                |
| unpickle             | 13.7 us                                                | 14.3 us: 1.05x slower                                                |
| xml_etree_iterparse  | 104 ms                                                 | 110 ms: 1.06x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.38 us: 1.07x slower                                                |
| json_dumps           | 12.6 ms                                                | 13.6 ms: 1.08x slower                                                |
| pickle_dict          | 31.1 us                                                | 33.7 us: 1.08x slower                                                |
| json_loads           | 26.5 us                                                | 29.0 us: 1.09x slower                                                |
| xml_etree_generate   | 76.2 ms                                                | 93.1 ms: 1.22x slower                                                |
| unpickle_pure_python | 228 us                                                 | 298 us: 1.31x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 74.1 ms: 1.38x slower                                                |
| pickle_pure_python   | 306 us                                                 | 452 us: 1.48x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.83 ms: 1.03x faster                                                |
| python_startup         | 8.52 ms                                                | 14.2 ms: 1.67x slower                                                |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 62.6 ms: 1.21x slower                                                |
| genshi_text     | 21.6 ms                                                | 30.1 ms: 1.39x slower                                                |
| django_template | 32.6 ms                                                | 45.8 ms: 1.40x slower                                                |
| mako            | 10.1 ms                                                | 14.7 ms: 1.46x slower                                                |
| Geometric mean  | (ref)                                                  | 1.36x slower                                                         |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| coverage                | 100 ms                                                 | 72.1 ms: 1.39x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                |
| gc_traversal            | 4.02 ms                                                | 3.71 ms: 1.08x faster                                                |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                 |
| asyncio_tcp             | 922 ms                                                 | 894 ms: 1.03x faster                                                 |
| python_startup_no_site  | 6.01 ms                                                | 5.83 ms: 1.03x faster                                                |
| unpickle_list           | 4.91 us                                                | 4.80 us: 1.02x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 163 ms: 1.03x slower                                                 |
| generators              | 73.5 ms                                                | 75.5 ms: 1.03x slower                                                |
| telco                   | 6.58 ms                                                | 6.78 ms: 1.03x slower                                                |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                |
| regex_dna               | 204 ms                                                 | 213 ms: 1.05x slower                                                 |
| unpickle                | 13.7 us                                                | 14.3 us: 1.05x slower                                                |
| meteor_contest          | 107 ms                                                 | 113 ms: 1.06x slower                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 110 ms: 1.06x slower                                                 |
| pickle_list             | 4.11 us                                                | 4.38 us: 1.07x slower                                                |
| json                    | 4.94 ms                                                | 5.32 ms: 1.08x slower                                                |
| json_dumps              | 12.6 ms                                                | 13.6 ms: 1.08x slower                                                |
| pickle_dict             | 31.1 us                                                | 33.7 us: 1.08x slower                                                |
| pathlib                 | 18.2 ms                                                | 19.9 ms: 1.09x slower                                                |
| mdp                     | 2.62 sec                                               | 2.85 sec: 1.09x slower                                               |
| json_loads              | 26.5 us                                                | 29.0 us: 1.09x slower                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.66 ms: 1.12x slower                                                |
| bench_thread_pool       | 819 us                                                 | 925 us: 1.13x slower                                                 |
| sympy_sum               | 167 ms                                                 | 188 ms: 1.13x slower                                                 |
| pylint                  | 465 ms                                                 | 526 ms: 1.13x slower                                                 |
| sympy_str               | 290 ms                                                 | 330 ms: 1.14x slower                                                 |
| async_generators        | 368 ms                                                 | 421 ms: 1.14x slower                                                 |
| sympy_expand            | 475 ms                                                 | 545 ms: 1.15x slower                                                 |
| djangocms               | 32.4 us                                                | 37.3 us: 1.15x slower                                                |
| regex_v8                | 22.0 ms                                                | 25.5 ms: 1.16x slower                                                |
| sympy_integrate         | 21.0 ms                                                | 24.3 ms: 1.16x slower                                                |
| dask                    | 360 ms                                                 | 421 ms: 1.17x slower                                                 |
| sqlalchemy_imperative   | 17.9 ms                                                | 21.0 ms: 1.17x slower                                                |
| aiohttp                 | 1.10 ms                                                | 1.29 ms: 1.17x slower                                                |
| nqueens                 | 83.4 ms                                                | 97.9 ms: 1.17x slower                                                |
| gunicorn                | 1.18 ms                                                | 1.39 ms: 1.18x slower                                                |
| dulwich_log             | 63.7 ms                                                | 75.5 ms: 1.19x slower                                                |
| flaskblogging           | 7.12 ms                                                | 8.53 ms: 1.20x slower                                                |
| sqlite_synth            | 2.52 us                                                | 3.02 us: 1.20x slower                                                |
| comprehensions          | 22.4 us                                                | 27.0 us: 1.20x slower                                                |
| genshi_xml              | 51.8 ms                                                | 62.6 ms: 1.21x slower                                                |
| sqlalchemy_declarative  | 138 ms                                                 | 168 ms: 1.21x slower                                                 |
| fannkuch                | 388 ms                                                 | 471 ms: 1.21x slower                                                 |
| coroutines              | 25.5 ms                                                | 31.0 ms: 1.22x slower                                                |
| docutils                | 2.63 sec                                               | 3.21 sec: 1.22x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 93.1 ms: 1.22x slower                                                |
| scimark_sparse_mat_mult | 4.50 ms                                                | 5.50 ms: 1.22x slower                                                |
| sqlglot_optimize        | 53.1 ms                                                | 65.5 ms: 1.23x slower                                                |
| deepcopy                | 342 us                                                 | 429 us: 1.25x slower                                                 |
| sqlglot_normalize       | 108 ms                                                 | 136 ms: 1.26x slower                                                 |
| scimark_fft             | 328 ms                                                 | 416 ms: 1.27x slower                                                 |
| regex_compile           | 138 ms                                                 | 176 ms: 1.27x slower                                                 |
| deepcopy_reduce         | 2.94 us                                                | 3.77 us: 1.28x slower                                                |
| pycparser               | 1.18 sec                                               | 1.52 sec: 1.29x slower                                               |
| 2to3                    | 259 ms                                                 | 335 ms: 1.29x slower                                                 |
| unpickle_pure_python    | 228 us                                                 | 298 us: 1.31x slower                                                 |
| async_tree_cpu_io_mixed | 739 ms                                                 | 975 ms: 1.32x slower                                                 |
| html5lib                | 64.5 ms                                                | 85.4 ms: 1.32x slower                                                |
| deepcopy_memo           | 37.0 us                                                | 49.8 us: 1.35x slower                                                |
| pprint_pformat          | 1.46 sec                                               | 1.97 sec: 1.35x slower                                               |
| tornado_http            | 96.3 ms                                                | 131 ms: 1.36x slower                                                 |
| pprint_safe_repr        | 701 ms                                                 | 953 ms: 1.36x slower                                                 |
| logging_format          | 6.68 us                                                | 9.16 us: 1.37x slower                                                |
| xml_etree_process       | 53.9 ms                                                | 74.1 ms: 1.38x slower                                                |
| thrift                  | 756 us                                                 | 1.04 ms: 1.38x slower                                                |
| chameleon               | 6.47 ms                                                | 8.93 ms: 1.38x slower                                                |
| async_tree_none         | 526 ms                                                 | 732 ms: 1.39x slower                                                 |
| logging_simple          | 6.03 us                                                | 8.40 us: 1.39x slower                                                |
| async_tree_memoization  | 627 ms                                                 | 873 ms: 1.39x slower                                                 |
| genshi_text             | 21.6 ms                                                | 30.1 ms: 1.39x slower                                                |
| float                   | 77.2 ms                                                | 108 ms: 1.40x slower                                                 |
| async_tree_io           | 1.30 sec                                               | 1.82 sec: 1.40x slower                                               |
| django_template         | 32.6 ms                                                | 45.8 ms: 1.40x slower                                                |
| spectral_norm           | 100 ms                                                 | 142 ms: 1.42x slower                                                 |
| sqlglot_transpile       | 1.70 ms                                                | 2.44 ms: 1.43x slower                                                |
| scimark_lu              | 110 ms                                                 | 159 ms: 1.45x slower                                                 |
| sqlglot_parse           | 1.40 ms                                                | 2.04 ms: 1.46x slower                                                |
| mako                    | 10.1 ms                                                | 14.7 ms: 1.46x slower                                                |
| nbody                   | 93.1 ms                                                | 137 ms: 1.48x slower                                                 |
| hexiom                  | 6.37 ms                                                | 9.41 ms: 1.48x slower                                                |
| pickle_pure_python      | 306 us                                                 | 452 us: 1.48x slower                                                 |
| chaos                   | 69.2 ms                                                | 105 ms: 1.51x slower                                                 |
| crypto_pyaes            | 74.7 ms                                                | 114 ms: 1.53x slower                                                 |
| raytrace                | 297 ms                                                 | 462 ms: 1.56x slower                                                 |
| unpack_sequence         | 43.1 ns                                                | 67.6 ns: 1.57x slower                                                |
| pyflate                 | 418 ms                                                 | 660 ms: 1.58x slower                                                 |
| richards                | 45.7 ms                                                | 73.1 ms: 1.60x slower                                                |
| scimark_monte_carlo     | 68.1 ms                                                | 109 ms: 1.60x slower                                                 |
| go                      | 140 ms                                                 | 227 ms: 1.62x slower                                                 |
| scimark_sor             | 118 ms                                                 | 194 ms: 1.64x slower                                                 |
| python_startup          | 8.52 ms                                                | 14.2 ms: 1.67x slower                                                |
| logging_silent          | 101 ns                                                 | 175 ns: 1.73x slower                                                 |
| deltablue               | 3.67 ms                                                | 7.35 ms: 2.00x slower                                                |
| Geometric mean          | (ref)                                                  | 1.24x slower                                                         |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.19x
