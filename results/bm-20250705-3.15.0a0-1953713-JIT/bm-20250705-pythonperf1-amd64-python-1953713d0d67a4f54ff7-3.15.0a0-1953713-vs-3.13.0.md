# Results vs. 3.13.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.090x faster
- HPT reliability: 91.01%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| sphinx         | 617 ms                                                      | 639 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 52.3 ms: 1.27x faster                                                      |
| float          | 50.8 ms                                                     | 42.8 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.6 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.22x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.11 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 203 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.44 ms: 1.21x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 486 us: 17.42x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| mdp                        | 1.43 sec                                                    | 798 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| nbody                      | 66.3 ms                                                     | 52.3 ms: 1.27x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.22x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.44 ms: 1.21x faster                                                      |
| float                      | 50.8 ms                                                     | 42.8 ms: 1.19x faster                                                      |
| scimark_fft                | 175 ms                                                      | 151 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.27 ms: 1.15x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.25 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                       |
| go                         | 84.7 ms                                                     | 75.0 ms: 1.13x faster                                                      |
| fannkuch                   | 252 ms                                                      | 224 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| pyflate                    | 283 ms                                                      | 252 ms: 1.12x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.61 sec: 1.10x faster                                                     |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 449 ms: 1.08x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                      |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 927 ms: 1.05x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.05x faster                                                     |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.6 ms: 1.03x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 62.1 ms: 1.02x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.0 ms: 1.01x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.11 ms: 1.01x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 75.2 ms: 1.01x faster                                                      |
| logging_silent             | 54.6 ns                                                     | 54.2 ns: 1.01x faster                                                      |
| richards                   | 26.3 ms                                                     | 26.4 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.3 ms: 1.01x slower                                                      |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.02x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.3 ms: 1.02x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.3 ms: 1.02x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 639 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.65 us: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 851 us: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.06 ms: 1.06x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.12 us: 1.06x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.6 ms: 1.06x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.61 us: 1.07x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.7 ms: 1.07x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 203 us: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.13 ms: 1.13x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 95.3 ms: 1.13x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.6 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.16x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 444 us: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (7): pylint, pidigits, pycparser, shortest_path, html5lib, typing_runtime_protocols, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 91.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown