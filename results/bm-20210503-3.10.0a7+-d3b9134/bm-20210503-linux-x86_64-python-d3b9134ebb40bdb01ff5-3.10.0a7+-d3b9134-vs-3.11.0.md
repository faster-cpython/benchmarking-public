
# Results vs. 3.11.0

- fork: python
- ref: d3b9134ebb40bdb01ff5
- machine: linux-x86_64
- commit hash: d3b9134
- commit date: 2021-05-03
- overall geometric mean: 1.23x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 333 ms: 1.29x slower                                                   |
| docutils       | 2.63 sec                                               | 3.17 sec: 1.21x slower                                                 |
| html5lib       | 64.5 ms                                                | 86.5 ms: 1.34x slower                                                  |
| tornado_http   | 96.3 ms                                                | 129 ms: 1.34x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                   |
| float          | 77.2 ms                                                | 107 ms: 1.39x slower                                                   |
| nbody          | 93.1 ms                                                | 141 ms: 1.51x slower                                                   |
| Geometric mean | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.24 ms: 1.23x faster                                                  |
| regex_dna      | 204 ms                                                 | 211 ms: 1.04x slower                                                   |
| regex_v8       | 22.0 ms                                                | 25.4 ms: 1.15x slower                                                  |
| regex_compile  | 138 ms                                                 | 171 ms: 1.24x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 26.9 us: 1.16x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                   |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                                  |
| unpickle             | 13.7 us                                                | 14.3 us: 1.05x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 110 ms: 1.06x slower                                                   |
| json_loads           | 26.5 us                                                | 28.4 us: 1.07x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.45 us: 1.08x slower                                                  |
| json_dumps           | 12.6 ms                                                | 13.7 ms: 1.09x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 92.4 ms: 1.21x slower                                                  |
| unpickle_pure_python | 228 us                                                 | 294 us: 1.29x slower                                                   |
| xml_etree_process    | 53.9 ms                                                | 73.2 ms: 1.36x slower                                                  |
| pickle_pure_python   | 306 us                                                 | 451 us: 1.47x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.79 ms: 1.04x faster                                                  |
| python_startup         | 8.52 ms                                                | 15.2 ms: 1.79x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 63.2 ms: 1.22x slower                                                  |
| genshi_text     | 21.6 ms                                                | 30.1 ms: 1.40x slower                                                  |
| django_template | 32.6 ms                                                | 46.2 ms: 1.42x slower                                                  |
| mako            | 10.1 ms                                                | 14.7 ms: 1.45x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.37x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| coverage                | 100 ms                                                 | 65.8 ms: 1.52x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.24 ms: 1.23x faster                                                  |
| generators              | 73.5 ms                                                | 61.6 ms: 1.19x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.48 ms: 1.16x faster                                                  |
| pickle_dict             | 31.1 us                                                | 26.9 us: 1.16x faster                                                  |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                   |
| python_startup_no_site  | 6.01 ms                                                | 5.79 ms: 1.04x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 893 ms: 1.03x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 154 ms: 1.03x faster                                                   |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                                  |
| telco                   | 6.58 ms                                                | 6.74 ms: 1.02x slower                                                  |
| regex_dna               | 204 ms                                                 | 211 ms: 1.04x slower                                                   |
| pathlib                 | 18.2 ms                                                | 18.9 ms: 1.04x slower                                                  |
| meteor_contest          | 107 ms                                                 | 111 ms: 1.04x slower                                                   |
| unpickle                | 13.7 us                                                | 14.3 us: 1.05x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 110 ms: 1.06x slower                                                   |
| json                    | 4.94 ms                                                | 5.26 ms: 1.06x slower                                                  |
| json_loads              | 26.5 us                                                | 28.4 us: 1.07x slower                                                  |
| mdp                     | 2.62 sec                                               | 2.82 sec: 1.08x slower                                                 |
| pickle_list             | 4.11 us                                                | 4.45 us: 1.08x slower                                                  |
| json_dumps              | 12.6 ms                                                | 13.7 ms: 1.09x slower                                                  |
| sympy_sum               | 167 ms                                                 | 183 ms: 1.10x slower                                                   |
| pylint                  | 465 ms                                                 | 512 ms: 1.10x slower                                                   |
| sympy_str               | 290 ms                                                 | 322 ms: 1.11x slower                                                   |
| sympy_expand            | 475 ms                                                 | 531 ms: 1.12x slower                                                   |
| djangocms               | 32.4 us                                                | 36.4 us: 1.12x slower                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.67 ms: 1.13x slower                                                  |
| async_generators        | 368 ms                                                 | 420 ms: 1.14x slower                                                   |
| sympy_integrate         | 21.0 ms                                                | 23.9 ms: 1.14x slower                                                  |
| regex_v8                | 22.0 ms                                                | 25.4 ms: 1.15x slower                                                  |
| nqueens                 | 83.4 ms                                                | 97.2 ms: 1.17x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.94 us: 1.17x slower                                                  |
| bench_thread_pool       | 819 us                                                 | 960 us: 1.17x slower                                                   |
| dulwich_log             | 63.7 ms                                                | 75.6 ms: 1.19x slower                                                  |
| coroutines              | 25.5 ms                                                | 30.4 ms: 1.19x slower                                                  |
| fannkuch                | 388 ms                                                 | 467 ms: 1.21x slower                                                   |
| docutils                | 2.63 sec                                               | 3.17 sec: 1.21x slower                                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 5.44 ms: 1.21x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 92.4 ms: 1.21x slower                                                  |
| genshi_xml              | 51.8 ms                                                | 63.2 ms: 1.22x slower                                                  |
| regex_compile           | 138 ms                                                 | 171 ms: 1.24x slower                                                   |
| deepcopy                | 342 us                                                 | 423 us: 1.24x slower                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 66.1 ms: 1.25x slower                                                  |
| scimark_fft             | 328 ms                                                 | 411 ms: 1.25x slower                                                   |
| sqlglot_normalize       | 108 ms                                                 | 135 ms: 1.25x slower                                                   |
| deepcopy_reduce         | 2.94 us                                                | 3.73 us: 1.27x slower                                                  |
| pycparser               | 1.18 sec                                               | 1.52 sec: 1.29x slower                                                 |
| 2to3                    | 259 ms                                                 | 333 ms: 1.29x slower                                                   |
| unpickle_pure_python    | 228 us                                                 | 294 us: 1.29x slower                                                   |
| logging_format          | 6.68 us                                                | 8.72 us: 1.30x slower                                                  |
| deepcopy_memo           | 37.0 us                                                | 48.8 us: 1.32x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 977 ms: 1.32x slower                                                   |
| logging_simple          | 6.03 us                                                | 8.01 us: 1.33x slower                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.94 sec: 1.33x slower                                                 |
| thrift                  | 756 us                                                 | 1.01 ms: 1.34x slower                                                  |
| pprint_safe_repr        | 701 ms                                                 | 938 ms: 1.34x slower                                                   |
| html5lib                | 64.5 ms                                                | 86.5 ms: 1.34x slower                                                  |
| tornado_http            | 96.3 ms                                                | 129 ms: 1.34x slower                                                   |
| async_tree_memoization  | 627 ms                                                 | 848 ms: 1.35x slower                                                   |
| async_tree_none         | 526 ms                                                 | 712 ms: 1.35x slower                                                   |
| xml_etree_process       | 53.9 ms                                                | 73.2 ms: 1.36x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 59.0 ns: 1.37x slower                                                  |
| float                   | 77.2 ms                                                | 107 ms: 1.39x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.80 sec: 1.39x slower                                                 |
| genshi_text             | 21.6 ms                                                | 30.1 ms: 1.40x slower                                                  |
| django_template         | 32.6 ms                                                | 46.2 ms: 1.42x slower                                                  |
| hexiom                  | 6.37 ms                                                | 9.25 ms: 1.45x slower                                                  |
| mako                    | 10.1 ms                                                | 14.7 ms: 1.45x slower                                                  |
| scimark_lu              | 110 ms                                                 | 160 ms: 1.46x slower                                                   |
| pickle_pure_python      | 306 us                                                 | 451 us: 1.47x slower                                                   |
| spectral_norm           | 100 ms                                                 | 149 ms: 1.49x slower                                                   |
| nbody                   | 93.1 ms                                                | 141 ms: 1.51x slower                                                   |
| chaos                   | 69.2 ms                                                | 106 ms: 1.53x slower                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 106 ms: 1.56x slower                                                   |
| raytrace                | 297 ms                                                 | 466 ms: 1.57x slower                                                   |
| crypto_pyaes            | 74.7 ms                                                | 118 ms: 1.58x slower                                                   |
| pyflate                 | 418 ms                                                 | 660 ms: 1.58x slower                                                   |
| richards                | 45.7 ms                                                | 72.6 ms: 1.59x slower                                                  |
| go                      | 140 ms                                                 | 224 ms: 1.60x slower                                                   |
| scimark_sor             | 118 ms                                                 | 195 ms: 1.65x slower                                                   |
| logging_silent          | 101 ns                                                 | 169 ns: 1.67x slower                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 2.97 ms: 1.75x slower                                                  |
| python_startup          | 8.52 ms                                                | 15.2 ms: 1.79x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 2.57 ms: 1.83x slower                                                  |
| deltablue               | 3.67 ms                                                | 7.29 ms: 1.98x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.23x slower                                                           |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, comprehensions, dask, flaskblogging, gunicorn, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.18x
