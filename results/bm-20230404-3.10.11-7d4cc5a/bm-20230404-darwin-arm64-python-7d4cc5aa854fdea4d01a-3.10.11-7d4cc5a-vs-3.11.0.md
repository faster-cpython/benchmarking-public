
# Results vs. 3.11.0

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: darwin-arm64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.22x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 203 ms: 1.26x slower                                                 |
| chameleon      | 4.60 ms                                                | 5.75 ms: 1.25x slower                                                |
| docutils       | 1.47 sec                                               | 1.79 sec: 1.22x slower                                               |
| html5lib       | 34.7 ms                                                | 47.8 ms: 1.38x slower                                                |
| tornado_http   | 71.5 ms                                                | 91.2 ms: 1.27x slower                                                |
| Geometric mean | (ref)                                                  | 1.27x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                 |
| float          | 53.0 ms                                                | 72.2 ms: 1.36x slower                                                |
| nbody          | 65.6 ms                                                | 94.0 ms: 1.43x slower                                                |
| Geometric mean | (ref)                                                  | 1.25x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.69 ms: 1.02x slower                                                |
| regex_v8       | 16.1 ms                                                | 18.0 ms: 1.12x slower                                                |
| regex_dna      | 152 ms                                                 | 185 ms: 1.22x slower                                                 |
| regex_compile  | 76.7 ms                                                | 96.9 ms: 1.26x slower                                                |
| Geometric mean | (ref)                                                  | 1.15x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_list        | 2.65 us                                                | 2.69 us: 1.02x slower                                                |
| unpickle             | 9.67 us                                                | 9.89 us: 1.02x slower                                                |
| pickle_list          | 2.81 us                                                | 2.90 us: 1.03x slower                                                |
| xml_etree_iterparse  | 70.1 ms                                                | 73.2 ms: 1.04x slower                                                |
| json_loads           | 16.1 us                                                | 16.8 us: 1.05x slower                                                |
| pickle_dict          | 18.0 us                                                | 18.8 us: 1.05x slower                                                |
| pickle               | 7.15 us                                                | 7.56 us: 1.06x slower                                                |
| json_dumps           | 7.63 ms                                                | 8.27 ms: 1.08x slower                                                |
| xml_etree_generate   | 48.3 ms                                                | 54.3 ms: 1.13x slower                                                |
| unpickle_pure_python | 159 us                                                 | 204 us: 1.28x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 44.9 ms: 1.28x slower                                                |
| pickle_pure_python   | 201 us                                                 | 285 us: 1.42x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.13 ms: 1.11x faster                                                |
| python_startup         | 12.4 ms                                                | 12.1 ms: 1.02x faster                                                |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 18.2 ms: 1.19x slower                                                |
| mako            | 8.53 ms                                                | 10.6 ms: 1.24x slower                                                |
| genshi_xml      | 29.8 ms                                                | 37.3 ms: 1.25x slower                                                |
| django_template | 21.0 ms                                                | 27.1 ms: 1.29x slower                                                |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                         |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| coverage                | 58.4 ms                                                | 41.9 ms: 1.40x faster                                                |
| python_startup_no_site  | 10.2 ms                                                | 9.13 ms: 1.11x faster                                                |
| bench_mp_pool           | 43.9 ms                                                | 40.2 ms: 1.09x faster                                                |
| python_startup          | 12.4 ms                                                | 12.1 ms: 1.02x faster                                                |
| gc_traversal            | 2.42 ms                                                | 2.39 ms: 1.01x faster                                                |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                 |
| unpickle_list           | 2.65 us                                                | 2.69 us: 1.02x slower                                                |
| unpickle                | 9.67 us                                                | 9.89 us: 1.02x slower                                                |
| regex_effbot            | 2.63 ms                                                | 2.69 ms: 1.02x slower                                                |
| asyncio_tcp             | 651 ms                                                 | 669 ms: 1.03x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.90 us: 1.03x slower                                                |
| pathlib                 | 27.2 ms                                                | 28.3 ms: 1.04x slower                                                |
| xml_etree_iterparse     | 70.1 ms                                                | 73.2 ms: 1.04x slower                                                |
| json_loads              | 16.1 us                                                | 16.8 us: 1.05x slower                                                |
| pickle_dict             | 18.0 us                                                | 18.8 us: 1.05x slower                                                |
| pickle                  | 7.15 us                                                | 7.56 us: 1.06x slower                                                |
| meteor_contest          | 73.5 ms                                                | 78.0 ms: 1.06x slower                                                |
| telco                   | 3.41 ms                                                | 3.63 ms: 1.07x slower                                                |
| mdp                     | 1.55 sec                                               | 1.67 sec: 1.08x slower                                               |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.46 ms: 1.08x slower                                                |
| json_dumps              | 7.63 ms                                                | 8.27 ms: 1.08x slower                                                |
| json                    | 2.78 ms                                                | 3.06 ms: 1.10x slower                                                |
| comprehensions          | 16.1 us                                                | 17.9 us: 1.11x slower                                                |
| regex_v8                | 16.1 ms                                                | 18.0 ms: 1.12x slower                                                |
| bench_thread_pool       | 474 us                                                 | 532 us: 1.12x slower                                                 |
| unpack_sequence         | 34.1 ns                                                | 38.3 ns: 1.12x slower                                                |
| xml_etree_generate      | 48.3 ms                                                | 54.3 ms: 1.13x slower                                                |
| sympy_sum               | 85.5 ms                                                | 96.4 ms: 1.13x slower                                                |
| sympy_str               | 151 ms                                                 | 170 ms: 1.13x slower                                                 |
| pylint                  | 272 ms                                                 | 307 ms: 1.13x slower                                                 |
| coroutines              | 17.8 ms                                                | 20.1 ms: 1.13x slower                                                |
| generators              | 28.8 ms                                                | 32.7 ms: 1.14x slower                                                |
| flaskblogging           | 2.43 ms                                                | 2.76 ms: 1.14x slower                                                |
| nqueens                 | 59.8 ms                                                | 68.0 ms: 1.14x slower                                                |
| sympy_expand            | 242 ms                                                 | 277 ms: 1.14x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 196 ms: 1.15x slower                                                 |
| scimark_fft             | 200 ms                                                 | 231 ms: 1.16x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 13.4 ms: 1.16x slower                                                |
| sqlite_synth            | 1.27 us                                                | 1.48 us: 1.16x slower                                                |
| async_generators        | 196 ms                                                 | 233 ms: 1.19x slower                                                 |
| genshi_text             | 15.3 ms                                                | 18.2 ms: 1.19x slower                                                |
| sqlalchemy_declarative  | 62.6 ms                                                | 75.0 ms: 1.20x slower                                                |
| aiohttp                 | 1.05 ms                                                | 1.26 ms: 1.20x slower                                                |
| gunicorn                | 1.11 ms                                                | 1.34 ms: 1.21x slower                                                |
| regex_dna               | 152 ms                                                 | 185 ms: 1.22x slower                                                 |
| dulwich_log             | 30.3 ms                                                | 36.9 ms: 1.22x slower                                                |
| docutils                | 1.47 sec                                               | 1.79 sec: 1.22x slower                                               |
| fannkuch                | 261 ms                                                 | 319 ms: 1.22x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 38.0 ms: 1.22x slower                                                |
| create_gc_cycles        | 716 us                                                 | 874 us: 1.22x slower                                                 |
| mako                    | 8.53 ms                                                | 10.6 ms: 1.24x slower                                                |
| deepcopy_reduce         | 1.91 us                                                | 2.38 us: 1.24x slower                                                |
| chameleon               | 4.60 ms                                                | 5.75 ms: 1.25x slower                                                |
| genshi_xml              | 29.8 ms                                                | 37.3 ms: 1.25x slower                                                |
| deepcopy                | 223 us                                                 | 279 us: 1.25x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 668 ms: 1.25x slower                                                 |
| sqlalchemy_imperative   | 7.20 ms                                                | 9.01 ms: 1.25x slower                                                |
| 2to3                    | 161 ms                                                 | 203 ms: 1.26x slower                                                 |
| regex_compile           | 76.7 ms                                                | 96.9 ms: 1.26x slower                                                |
| tornado_http            | 71.5 ms                                                | 91.2 ms: 1.27x slower                                                |
| unpickle_pure_python    | 159 us                                                 | 204 us: 1.28x slower                                                 |
| xml_etree_process       | 35.1 ms                                                | 44.9 ms: 1.28x slower                                                |
| django_template         | 21.0 ms                                                | 27.1 ms: 1.29x slower                                                |
| pprint_safe_repr        | 466 ms                                                 | 602 ms: 1.29x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 1.23 sec: 1.29x slower                                               |
| pycparser               | 698 ms                                                 | 910 ms: 1.30x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 34.5 us: 1.31x slower                                                |
| logging_simple          | 3.55 us                                                | 4.65 us: 1.31x slower                                                |
| thrift                  | 442 us                                                 | 580 us: 1.31x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 96.4 ms: 1.33x slower                                                |
| logging_format          | 3.78 us                                                | 5.05 us: 1.34x slower                                                |
| hexiom                  | 4.72 ms                                                | 6.33 ms: 1.34x slower                                                |
| float                   | 53.0 ms                                                | 72.2 ms: 1.36x slower                                                |
| sqlglot_transpile       | 1.12 ms                                                | 1.53 ms: 1.36x slower                                                |
| chaos                   | 49.4 ms                                                | 68.0 ms: 1.38x slower                                                |
| html5lib                | 34.7 ms                                                | 47.8 ms: 1.38x slower                                                |
| sqlglot_parse           | 959 us                                                 | 1.33 ms: 1.39x slower                                                |
| async_tree_none         | 286 ms                                                 | 399 ms: 1.40x slower                                                 |
| pickle_pure_python      | 201 us                                                 | 285 us: 1.42x slower                                                 |
| nbody                   | 65.6 ms                                                | 94.0 ms: 1.43x slower                                                |
| async_tree_io           | 704 ms                                                 | 1.02 sec: 1.44x slower                                               |
| async_tree_memoization  | 336 ms                                                 | 490 ms: 1.46x slower                                                 |
| pyflate                 | 310 ms                                                 | 455 ms: 1.47x slower                                                 |
| scimark_lu              | 73.3 ms                                                | 110 ms: 1.50x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 78.3 ms: 1.51x slower                                                |
| go                      | 109 ms                                                 | 165 ms: 1.52x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 126 ms: 1.53x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 72.3 ms: 1.56x slower                                                |
| richards                | 32.2 ms                                                | 50.7 ms: 1.57x slower                                                |
| mypy2                   | 195 ms                                                 | 307 ms: 1.58x slower                                                 |
| raytrace                | 207 ms                                                 | 331 ms: 1.60x slower                                                 |
| logging_silent          | 68.1 ns                                                | 120 ns: 1.75x slower                                                 |
| deltablue               | 2.81 ms                                                | 5.17 ms: 1.84x slower                                                |
| Geometric mean          | (ref)                                                  | 1.22x slower                                                         |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230404-3.10.11-7d4cc5a/bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.17x
