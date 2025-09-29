# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.036x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.81 sec: 1.84x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                      |
| sphinx         | 617 ms                                                      | 656 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 138 ms: 2.18x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 317 ms: 1.57x faster                                                       |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 188 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 307 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| async_generators           | 223 ms                                                      | 255 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                      |
| pidigits       | 146 ms                                                      | 137 ms: 1.07x faster                                                       |
| nbody          | 66.3 ms                                                     | 78.5 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.65 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 90.6 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 57.3 ms: 1.06x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.06 ms: 1.02x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.7 ms: 1.02x faster                                                      |
| json_loads           | 15.1 us                                                     | 16.5 us: 1.09x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 60.6 ms: 1.13x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 150 us: 1.15x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 43.2 ms: 1.18x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 223 us: 1.20x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 18.5 ms: 1.21x slower                                                      |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                      |
| mako            | 6.56 ms                                                     | 9.65 ms: 1.47x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.26x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 569 us: 14.88x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.7 ms: 2.63x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 138 ms: 2.18x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.23 ms: 1.60x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 317 ms: 1.57x faster                                                       |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 188 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.06 sec: 1.35x faster                                                     |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 307 ms: 1.25x faster                                                       |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.8 us: 1.22x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.00 ms: 1.22x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.33 us: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 74.7 ms: 1.13x faster                                                      |
| float                      | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                      |
| pidigits                   | 146 ms                                                      | 137 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 57.3 ms: 1.06x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.65 ms: 1.02x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.06 ms: 1.02x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.7 ms: 1.02x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.99 us: 1.01x faster                                                      |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.00 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.4 ms: 1.03x slower                                                      |
| go                         | 84.7 ms                                                     | 88.5 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                      |
| sphinx                     | 617 ms                                                      | 656 ms: 1.06x slower                                                       |
| pyflate                    | 283 ms                                                      | 302 ms: 1.07x slower                                                       |
| scimark_fft                | 175 ms                                                      | 188 ms: 1.07x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 82.2 ms: 1.08x slower                                                      |
| sympy_str                  | 167 ms                                                      | 181 ms: 1.09x slower                                                       |
| sympy_expand               | 286 ms                                                      | 311 ms: 1.09x slower                                                       |
| json_loads                 | 15.1 us                                                     | 16.5 us: 1.09x slower                                                      |
| generators                 | 19.0 ms                                                     | 20.7 ms: 1.09x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 60.0 ns: 1.10x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.37 us: 1.10x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 94.1 ms: 1.11x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 70.5 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 540 ms: 1.11x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 63.5 ms: 1.12x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 90.6 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.13x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.94 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 60.6 ms: 1.13x slower                                                      |
| async_generators           | 223 ms                                                      | 255 ms: 1.14x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.10 us: 1.15x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 150 us: 1.15x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.45 ms: 1.16x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 43.2 ms: 1.18x slower                                                      |
| nbody                      | 66.3 ms                                                     | 78.5 ms: 1.18x slower                                                      |
| chaos                      | 37.9 ms                                                     | 45.1 ms: 1.19x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 85.8 ms: 1.19x slower                                                      |
| fannkuch                   | 252 ms                                                      | 302 ms: 1.20x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.9 ms: 1.20x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 223 us: 1.20x slower                                                       |
| richards                   | 26.3 ms                                                     | 31.6 ms: 1.20x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 18.5 ms: 1.21x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 56.5 ms: 1.24x slower                                                      |
| richards_super             | 29.8 ms                                                     | 36.9 ms: 1.24x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 128 us: 1.24x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.36 ms: 1.25x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 71.4 ms: 1.27x slower                                                      |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.05 ms: 1.30x slower                                                      |
| raytrace                   | 153 ms                                                      | 210 ms: 1.37x slower                                                       |
| mako                       | 6.56 ms                                                     | 9.65 ms: 1.47x slower                                                      |
| coverage                   | 45.3 ms                                                     | 66.8 ms: 1.47x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.65 sec: 1.56x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.61 sec: 1.65x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| many_optionals             | 361 us                                                      | 629 us: 1.74x slower                                                       |
| shortest_path              | 355 ms                                                      | 645 ms: 1.82x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.81 sec: 1.84x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.44 sec: 1.89x slower                                                     |
| connected_components       | 320 ms                                                      | 613 ms: 1.92x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 35.0 ms: 3.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): pycparser, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x slower

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown