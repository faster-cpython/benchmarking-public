# Results vs. base

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-amd64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.035x faster
- HPT reliability: 96.29%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                                                                 | 251 ms: 1.11x slower                                                                                                       |
| docutils       | 1.70 sec                                                                                                               | 1.88 sec: 1.11x slower                                                                                                     |
| html5lib       | 40.3 ms                                                                                                                | 38.9 ms: 1.04x faster                                                                                                      |
| sphinx         | 668 ms                                                                                                                 | 762 ms: 1.14x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.08x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization  | 279 ms                                                                                                                 | 262 ms: 1.06x faster                                                                                                       |
| async_tree_none         | 220 ms                                                                                                                 | 210 ms: 1.05x faster                                                                                                       |
| async_tree_io           | 564 ms                                                                                                                 | 546 ms: 1.03x faster                                                                                                       |
| async_tree_io_tg        | 635 ms                                                                                                                 | 627 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed | 383 ms                                                                                                                 | 391 ms: 1.02x slower                                                                                                       |
| async_tree_none_tg      | 212 ms                                                                                                                 | 218 ms: 1.03x slower                                                                                                       |
| async_generators        | 248 ms                                                                                                                 | 259 ms: 1.05x slower                                                                                                       |
| Geometric mean          | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 79.6 ms                                                                                                                | 53.2 ms: 1.50x faster                                                                                                      |
| float          | 56.0 ms                                                                                                                | 47.4 ms: 1.18x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.21x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 91.5 ms                                                                                                                | 90.9 ms: 1.01x faster                                                                                                      |
| regex_effbot   | 1.62 ms                                                                                                                | 1.61 ms: 1.00x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.60 sec                                                                                                               | 1.27 sec: 1.27x faster                                                                                                     |
| xml_etree_process    | 40.5 ms                                                                                                                | 36.0 ms: 1.13x faster                                                                                                      |
| xml_etree_generate   | 57.4 ms                                                                                                                | 51.0 ms: 1.12x faster                                                                                                      |
| pickle_pure_python   | 229 us                                                                                                                 | 207 us: 1.10x faster                                                                                                       |
| unpickle_pure_python | 153 us                                                                                                                 | 144 us: 1.07x faster                                                                                                       |
| json_dumps           | 6.67 ms                                                                                                                | 6.42 ms: 1.04x faster                                                                                                      |
| xml_etree_iterparse  | 65.3 ms                                                                                                                | 63.2 ms: 1.03x faster                                                                                                      |
| json_loads           | 14.5 us                                                                                                                | 14.3 us: 1.01x faster                                                                                                      |
| xml_etree_parse      | 93.1 ms                                                                                                                | 94.4 ms: 1.01x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.08x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                                                                                | 24.9 ms: 1.02x slower                                                                                                      |
| python_startup_no_site | 17.6 ms                                                                                                                | 18.8 ms: 1.07x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.05x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.93 ms                                                                                                                | 5.04 ms: 1.37x faster                                                                                                      |
| django_template | 25.5 ms                                                                                                                | 26.7 ms: 1.05x slower                                                                                                      |
| genshi_text     | 16.9 ms                                                                                                                | 19.2 ms: 1.14x slower                                                                                                      |
| genshi_xml      | 35.1 ms                                                                                                                | 45.5 ms: 1.30x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 79.6 ms                                                                                                                | 53.2 ms: 1.50x faster                                                                                                      |
| scimark_sor              | 91.0 ms                                                                                                                | 64.3 ms: 1.42x faster                                                                                                      |
| mako                     | 6.93 ms                                                                                                                | 5.04 ms: 1.37x faster                                                                                                      |
| scimark_monte_carlo      | 48.0 ms                                                                                                                | 37.4 ms: 1.28x faster                                                                                                      |
| scimark_fft              | 196 ms                                                                                                                 | 153 ms: 1.28x faster                                                                                                       |
| deepcopy_memo            | 21.2 us                                                                                                                | 16.6 us: 1.28x faster                                                                                                      |
| tomli_loads              | 1.60 sec                                                                                                               | 1.27 sec: 1.27x faster                                                                                                     |
| spectral_norm            | 67.8 ms                                                                                                                | 54.9 ms: 1.24x faster                                                                                                      |
| pprint_pformat           | 1.12 sec                                                                                                               | 918 ms: 1.22x faster                                                                                                       |
| scimark_sparse_mat_mult  | 2.73 ms                                                                                                                | 2.25 ms: 1.21x faster                                                                                                      |
| pprint_safe_repr         | 545 ms                                                                                                                 | 453 ms: 1.20x faster                                                                                                       |
| crypto_pyaes             | 48.0 ms                                                                                                                | 39.9 ms: 1.20x faster                                                                                                      |
| float                    | 56.0 ms                                                                                                                | 47.4 ms: 1.18x faster                                                                                                      |
| fannkuch                 | 280 ms                                                                                                                 | 242 ms: 1.16x faster                                                                                                       |
| bpe_tokeniser            | 3.11 sec                                                                                                               | 2.70 sec: 1.16x faster                                                                                                     |
| logging_silent           | 64.6 ns                                                                                                                | 56.3 ns: 1.15x faster                                                                                                      |
| xml_etree_process        | 40.5 ms                                                                                                                | 36.0 ms: 1.13x faster                                                                                                      |
| xml_etree_generate       | 57.4 ms                                                                                                                | 51.0 ms: 1.12x faster                                                                                                      |
| telco                    | 4.81 ms                                                                                                                | 4.29 ms: 1.12x faster                                                                                                      |
| scimark_lu               | 60.6 ms                                                                                                                | 54.7 ms: 1.11x faster                                                                                                      |
| deepcopy_reduce          | 2.00 us                                                                                                                | 1.81 us: 1.11x faster                                                                                                      |
| pickle_pure_python       | 229 us                                                                                                                 | 207 us: 1.10x faster                                                                                                       |
| dulwich_log              | 43.4 ms                                                                                                                | 39.6 ms: 1.10x faster                                                                                                      |
| chaos                    | 44.8 ms                                                                                                                | 41.2 ms: 1.09x faster                                                                                                      |
| pyflate                  | 322 ms                                                                                                                 | 296 ms: 1.09x faster                                                                                                       |
| unpickle_pure_python     | 153 us                                                                                                                 | 144 us: 1.07x faster                                                                                                       |
| async_tree_memoization   | 279 ms                                                                                                                 | 262 ms: 1.06x faster                                                                                                       |
| meteor_contest           | 78.0 ms                                                                                                                | 73.5 ms: 1.06x faster                                                                                                      |
| connected_components     | 329 ms                                                                                                                 | 311 ms: 1.06x faster                                                                                                       |
| async_tree_none          | 220 ms                                                                                                                 | 210 ms: 1.05x faster                                                                                                       |
| shortest_path            | 362 ms                                                                                                                 | 345 ms: 1.05x faster                                                                                                       |
| sqlglot_parse            | 922 us                                                                                                                 | 880 us: 1.05x faster                                                                                                       |
| deepcopy                 | 196 us                                                                                                                 | 188 us: 1.04x faster                                                                                                       |
| k_core                   | 2.53 sec                                                                                                               | 2.43 sec: 1.04x faster                                                                                                     |
| json_dumps               | 6.67 ms                                                                                                                | 6.42 ms: 1.04x faster                                                                                                      |
| html5lib                 | 40.3 ms                                                                                                                | 38.9 ms: 1.04x faster                                                                                                      |
| async_tree_io            | 564 ms                                                                                                                 | 546 ms: 1.03x faster                                                                                                       |
| xml_etree_iterparse      | 65.3 ms                                                                                                                | 63.2 ms: 1.03x faster                                                                                                      |
| sqlite_synth             | 1.62 us                                                                                                                | 1.57 us: 1.03x faster                                                                                                      |
| comprehensions           | 12.0 us                                                                                                                | 11.7 us: 1.03x faster                                                                                                      |
| logging_simple           | 6.39 us                                                                                                                | 6.22 us: 1.03x faster                                                                                                      |
| logging_format           | 6.83 us                                                                                                                | 6.66 us: 1.02x faster                                                                                                      |
| pycparser                | 738 ms                                                                                                                 | 721 ms: 1.02x faster                                                                                                       |
| async_tree_io_tg         | 635 ms                                                                                                                 | 627 ms: 1.01x faster                                                                                                       |
| json_loads               | 14.5 us                                                                                                                | 14.3 us: 1.01x faster                                                                                                      |
| thrift                   | 530 us                                                                                                                 | 524 us: 1.01x faster                                                                                                       |
| nqueens                  | 65.0 ms                                                                                                                | 64.3 ms: 1.01x faster                                                                                                      |
| regex_compile            | 91.5 ms                                                                                                                | 90.9 ms: 1.01x faster                                                                                                      |
| regex_effbot             | 1.62 ms                                                                                                                | 1.61 ms: 1.00x faster                                                                                                      |
| coverage                 | 47.2 ms                                                                                                                | 47.4 ms: 1.00x slower                                                                                                      |
| xml_etree_parse          | 93.1 ms                                                                                                                | 94.4 ms: 1.01x slower                                                                                                      |
| typing_runtime_protocols | 113 us                                                                                                                 | 114 us: 1.02x slower                                                                                                       |
| bench_thread_pool        | 813 us                                                                                                                 | 827 us: 1.02x slower                                                                                                       |
| async_tree_cpu_io_mixed  | 383 ms                                                                                                                 | 391 ms: 1.02x slower                                                                                                       |
| python_startup           | 24.3 ms                                                                                                                | 24.9 ms: 1.02x slower                                                                                                      |
| sqlglot_transpile        | 1.14 ms                                                                                                                | 1.17 ms: 1.03x slower                                                                                                      |
| async_tree_none_tg       | 212 ms                                                                                                                 | 218 ms: 1.03x slower                                                                                                       |
| generators               | 21.7 ms                                                                                                                | 22.5 ms: 1.04x slower                                                                                                      |
| django_template          | 25.5 ms                                                                                                                | 26.7 ms: 1.05x slower                                                                                                      |
| async_generators         | 248 ms                                                                                                                 | 259 ms: 1.05x slower                                                                                                       |
| sympy_expand             | 307 ms                                                                                                                 | 321 ms: 1.05x slower                                                                                                       |
| richards_super           | 37.2 ms                                                                                                                | 39.0 ms: 1.05x slower                                                                                                      |
| sqlglot_normalize        | 198 ms                                                                                                                 | 208 ms: 1.05x slower                                                                                                       |
| mdp                      | 1.45 sec                                                                                                               | 1.53 sec: 1.05x slower                                                                                                     |
| richards                 | 32.9 ms                                                                                                                | 34.9 ms: 1.06x slower                                                                                                      |
| sympy_str                | 179 ms                                                                                                                 | 190 ms: 1.06x slower                                                                                                       |
| python_startup_no_site   | 17.6 ms                                                                                                                | 18.8 ms: 1.07x slower                                                                                                      |
| pylint                   | 225 ms                                                                                                                 | 243 ms: 1.08x slower                                                                                                       |
| docutils                 | 1.70 sec                                                                                                               | 1.88 sec: 1.11x slower                                                                                                     |
| 2to3                     | 227 ms                                                                                                                 | 251 ms: 1.11x slower                                                                                                       |
| raytrace                 | 200 ms                                                                                                                 | 222 ms: 1.11x slower                                                                                                       |
| sympy_sum                | 90.3 ms                                                                                                                | 101 ms: 1.12x slower                                                                                                       |
| bench_mp_pool            | 83.0 ms                                                                                                                | 93.3 ms: 1.12x slower                                                                                                      |
| genshi_text              | 16.9 ms                                                                                                                | 19.2 ms: 1.14x slower                                                                                                      |
| sphinx                   | 668 ms                                                                                                                 | 762 ms: 1.14x slower                                                                                                       |
| sqlglot_optimize         | 37.2 ms                                                                                                                | 42.6 ms: 1.14x slower                                                                                                      |
| hexiom                   | 4.49 ms                                                                                                                | 5.16 ms: 1.15x slower                                                                                                      |
| sympy_integrate          | 13.4 ms                                                                                                                | 15.6 ms: 1.16x slower                                                                                                      |
| genshi_xml               | 35.1 ms                                                                                                                | 45.5 ms: 1.30x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (13): create_gc_cycles, pathlib, async_tree_memoization_tg, regex_dna, deltablue, pidigits, regex_v8, async_tree_cpu_io_mixed_tg, go, gc_traversal, json, coroutines, asyncio_websockets

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 96.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown