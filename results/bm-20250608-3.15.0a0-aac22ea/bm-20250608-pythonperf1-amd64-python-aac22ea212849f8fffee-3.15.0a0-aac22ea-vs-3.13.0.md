# Results vs. 3.13.0

- fork: python
- ref: aac22ea212849f8fffee
- machine: windows-amd64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.030x slower
- HPT reliability: 98.41%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 402 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 212 ms: 1.25x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 233 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                      |
| nbody          | 66.3 ms                                                     | 64.8 ms: 1.02x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.13x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.33 ms: 1.02x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 137 us: 1.05x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 57.0 ms: 1.07x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.5 ms: 1.08x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 214 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.79 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| mdp                        | 1.43 sec                                                    | 815 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                       |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 402 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 212 ms: 1.25x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 57.5 ms: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.0 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.71 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.54 ms: 1.03x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.5 ms: 1.02x faster                                                      |
| nbody                      | 66.3 ms                                                     | 64.8 ms: 1.02x faster                                                      |
| scimark_fft                | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.4 ms: 1.01x faster                                                      |
| fannkuch                   | 252 ms                                                      | 253 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.9 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.72 sec: 1.02x slower                                                     |
| pyflate                    | 283 ms                                                      | 289 ms: 1.02x slower                                                       |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.33 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 366 ms: 1.03x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.6 ms: 1.03x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.79 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 88.1 ms: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| pycparser                  | 695 ms                                                      | 720 ms: 1.04x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 233 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.01 sec: 1.05x slower                                                     |
| hexiom                     | 3.84 ms                                                     | 4.04 ms: 1.05x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 137 us: 1.05x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.0 ms: 1.06x slower                                                      |
| connected_components       | 320 ms                                                      | 338 ms: 1.06x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| xml_etree_generate         | 53.5 ms                                                     | 57.0 ms: 1.07x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.5 ms: 1.08x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.4 ms: 1.09x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.33 us: 1.10x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 541 ms: 1.12x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.13x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 214 us: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.19x slower                                                      |
| raytrace                   | 153 ms                                                      | 183 ms: 1.19x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 444 us: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.58x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 315 ns: 5.77x slower                                                       |
| coverage                   | 45.3 ms                                                     | 299 ms: 6.60x slower                                                       |
| thrift                     | 8.47 ms                                                     | 93.6 ms: 11.06x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (6): pylint, genshi_text, regex_compile, sqlite_synth, genshi_xml, html5lib
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 98.41% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown