# Results vs. base

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                                                          | 172 ms: 1.07x slower                                                                                                |
| docutils       | 1.46 sec                                                                                                        | 1.52 sec: 1.05x slower                                                                                              |
| html5lib       | 31.6 ms                                                                                                         | 32.7 ms: 1.04x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.04x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager | 64.4 ms                                                                                                         | 63.6 ms: 1.01x faster                                                                                               |
| Geometric mean   | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (15): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_io_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_eager_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 50.1 ms                                                                                                         | 47.8 ms: 1.05x faster                                                                                               |
| nbody          | 60.6 ms                                                                                                         | 64.2 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.59 ms                                                                                                         | 2.59 ms: 1.00x slower                                                                                               |
| regex_dna      | 149 ms                                                                                                          | 153 ms: 1.02x slower                                                                                                |
| regex_compile  | 68.5 ms                                                                                                         | 73.7 ms: 1.08x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.49 sec                                                                                                        | 1.26 sec: 1.18x faster                                                                                              |
| unpickle_pure_python | 143 us                                                                                                          | 133 us: 1.08x faster                                                                                                |
| xml_etree_process    | 37.9 ms                                                                                                         | 36.4 ms: 1.04x faster                                                                                               |
| pickle_pure_python   | 181 us                                                                                                          | 175 us: 1.03x faster                                                                                                |
| json_dumps           | 6.40 ms                                                                                                         | 6.27 ms: 1.02x faster                                                                                               |
| xml_etree_iterparse  | 72.2 ms                                                                                                         | 71.4 ms: 1.01x faster                                                                                               |
| xml_etree_generate   | 53.8 ms                                                                                                         | 53.5 ms: 1.01x faster                                                                                               |
| json_loads           | 17.2 us                                                                                                         | 17.3 us: 1.00x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.04x faster                                                                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 12.7 ms                                                                                                         | 12.8 ms: 1.00x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.14 ms                                                                                                         | 6.51 ms: 1.10x faster                                                                                               |
| django_template | 19.9 ms                                                                                                         | 21.4 ms: 1.07x slower                                                                                               |
| genshi_text     | 14.1 ms                                                                                                         | 16.3 ms: 1.16x slower                                                                                               |
| genshi_xml      | 30.3 ms                                                                                                         | 40.0 ms: 1.32x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.11x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads              | 1.49 sec                                                                                                        | 1.26 sec: 1.18x faster                                                                                              |
| mako                     | 7.14 ms                                                                                                         | 6.51 ms: 1.10x faster                                                                                               |
| unpickle_pure_python     | 143 us                                                                                                          | 133 us: 1.08x faster                                                                                                |
| fannkuch                 | 261 ms                                                                                                          | 247 ms: 1.06x faster                                                                                                |
| float                    | 50.1 ms                                                                                                         | 47.8 ms: 1.05x faster                                                                                               |
| xml_etree_process        | 37.9 ms                                                                                                         | 36.4 ms: 1.04x faster                                                                                               |
| pickle_pure_python       | 181 us                                                                                                          | 175 us: 1.03x faster                                                                                                |
| json_dumps               | 6.40 ms                                                                                                         | 6.27 ms: 1.02x faster                                                                                               |
| pyflate                  | 322 ms                                                                                                          | 317 ms: 1.02x faster                                                                                                |
| thrift                   | 438 us                                                                                                          | 432 us: 1.01x faster                                                                                                |
| json                     | 2.97 ms                                                                                                         | 2.93 ms: 1.01x faster                                                                                               |
| telco                    | 4.62 ms                                                                                                         | 4.56 ms: 1.01x faster                                                                                               |
| async_tree_eager         | 64.4 ms                                                                                                         | 63.6 ms: 1.01x faster                                                                                               |
| xml_etree_iterparse      | 72.2 ms                                                                                                         | 71.4 ms: 1.01x faster                                                                                               |
| logging_simple           | 3.10 us                                                                                                         | 3.07 us: 1.01x faster                                                                                               |
| deepcopy_memo            | 17.0 us                                                                                                         | 16.8 us: 1.01x faster                                                                                               |
| coroutines               | 16.3 ms                                                                                                         | 16.2 ms: 1.01x faster                                                                                               |
| xml_etree_generate       | 53.8 ms                                                                                                         | 53.5 ms: 1.01x faster                                                                                               |
| asyncio_websockets       | 409 ms                                                                                                          | 409 ms: 1.00x faster                                                                                                |
| bpe_tokeniser            | 3.11 sec                                                                                                        | 3.11 sec: 1.00x slower                                                                                              |
| regex_effbot             | 2.59 ms                                                                                                         | 2.59 ms: 1.00x slower                                                                                               |
| python_startup_no_site   | 12.7 ms                                                                                                         | 12.8 ms: 1.00x slower                                                                                               |
| json_loads               | 17.2 us                                                                                                         | 17.3 us: 1.00x slower                                                                                               |
| create_gc_cycles         | 900 us                                                                                                          | 905 us: 1.00x slower                                                                                                |
| scimark_monte_carlo      | 43.7 ms                                                                                                         | 44.1 ms: 1.01x slower                                                                                               |
| coverage                 | 45.3 ms                                                                                                         | 45.7 ms: 1.01x slower                                                                                               |
| meteor_contest           | 71.2 ms                                                                                                         | 71.9 ms: 1.01x slower                                                                                               |
| richards_super           | 34.8 ms                                                                                                         | 35.2 ms: 1.01x slower                                                                                               |
| go                       | 100 ms                                                                                                          | 101 ms: 1.01x slower                                                                                                |
| spectral_norm            | 68.0 ms                                                                                                         | 68.8 ms: 1.01x slower                                                                                               |
| scimark_fft              | 189 ms                                                                                                          | 191 ms: 1.01x slower                                                                                                |
| pathlib                  | 23.5 ms                                                                                                         | 23.8 ms: 1.02x slower                                                                                               |
| dask                     | 221 ms                                                                                                          | 225 ms: 1.02x slower                                                                                                |
| mdp                      | 1.42 sec                                                                                                        | 1.45 sec: 1.02x slower                                                                                              |
| generators               | 22.8 ms                                                                                                         | 23.2 ms: 1.02x slower                                                                                               |
| regex_dna                | 149 ms                                                                                                          | 153 ms: 1.02x slower                                                                                                |
| sympy_str                | 135 ms                                                                                                          | 139 ms: 1.03x slower                                                                                                |
| typing_runtime_protocols | 91.9 us                                                                                                         | 94.6 us: 1.03x slower                                                                                               |
| pprint_safe_repr         | 465 ms                                                                                                          | 480 ms: 1.03x slower                                                                                                |
| sympy_sum                | 70.6 ms                                                                                                         | 72.9 ms: 1.03x slower                                                                                               |
| crypto_pyaes             | 50.5 ms                                                                                                         | 52.2 ms: 1.03x slower                                                                                               |
| logging_silent           | 59.4 ns                                                                                                         | 61.5 ns: 1.04x slower                                                                                               |
| html5lib                 | 31.6 ms                                                                                                         | 32.7 ms: 1.04x slower                                                                                               |
| async_generators         | 283 ms                                                                                                          | 293 ms: 1.04x slower                                                                                                |
| bench_mp_pool            | 48.4 ms                                                                                                         | 50.2 ms: 1.04x slower                                                                                               |
| scimark_sparse_mat_mult  | 2.91 ms                                                                                                         | 3.03 ms: 1.04x slower                                                                                               |
| pprint_pformat           | 948 ms                                                                                                          | 988 ms: 1.04x slower                                                                                                |
| sympy_expand             | 231 ms                                                                                                          | 241 ms: 1.04x slower                                                                                                |
| deepcopy_reduce          | 1.50 us                                                                                                         | 1.56 us: 1.04x slower                                                                                               |
| sqlglot_normalize        | 169 ms                                                                                                          | 176 ms: 1.05x slower                                                                                                |
| bench_thread_pool        | 455 us                                                                                                          | 476 us: 1.05x slower                                                                                                |
| docutils                 | 1.46 sec                                                                                                        | 1.52 sec: 1.05x slower                                                                                              |
| sympy_integrate          | 10.5 ms                                                                                                         | 11.0 ms: 1.05x slower                                                                                               |
| sqlglot_optimize         | 31.5 ms                                                                                                         | 33.2 ms: 1.06x slower                                                                                               |
| deepcopy                 | 145 us                                                                                                          | 153 us: 1.06x slower                                                                                                |
| pycparser                | 639 ms                                                                                                          | 676 ms: 1.06x slower                                                                                                |
| scimark_sor              | 96.3 ms                                                                                                         | 102 ms: 1.06x slower                                                                                                |
| nbody                    | 60.6 ms                                                                                                         | 64.2 ms: 1.06x slower                                                                                               |
| gc_traversal             | 2.46 ms                                                                                                         | 2.61 ms: 1.06x slower                                                                                               |
| 2to3                     | 161 ms                                                                                                          | 172 ms: 1.07x slower                                                                                                |
| nqueens                  | 54.2 ms                                                                                                         | 57.8 ms: 1.07x slower                                                                                               |
| django_template          | 19.9 ms                                                                                                         | 21.4 ms: 1.07x slower                                                                                               |
| regex_compile            | 68.5 ms                                                                                                         | 73.7 ms: 1.08x slower                                                                                               |
| hexiom                   | 4.08 ms                                                                                                         | 4.42 ms: 1.08x slower                                                                                               |
| chaos                    | 36.1 ms                                                                                                         | 39.3 ms: 1.09x slower                                                                                               |
| raytrace                 | 151 ms                                                                                                          | 165 ms: 1.10x slower                                                                                                |
| deltablue                | 2.11 ms                                                                                                         | 2.33 ms: 1.10x slower                                                                                               |
| sqlglot_transpile        | 906 us                                                                                                          | 1.00 ms: 1.11x slower                                                                                               |
| sqlglot_parse            | 746 us                                                                                                          | 834 us: 1.12x slower                                                                                                |
| comprehensions           | 10.7 us                                                                                                         | 12.3 us: 1.15x slower                                                                                               |
| genshi_text              | 14.1 ms                                                                                                         | 16.3 ms: 1.16x slower                                                                                               |
| scimark_lu               | 70.8 ms                                                                                                         | 82.8 ms: 1.17x slower                                                                                               |
| genshi_xml               | 30.3 ms                                                                                                         | 40.0 ms: 1.32x slower                                                                                               |
| Geometric mean           | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (25): python_startup, async_tree_io, asyncio_tcp, asyncio_tcp_ssl, richards, async_tree_none_tg, async_tree_cpu_io_mixed, logging_format, xml_etree_parse, async_tree_none, async_tree_eager_io_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, pidigits, regex_v8, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_eager_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_memoization, tornado_http, async_tree_eager_io, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x