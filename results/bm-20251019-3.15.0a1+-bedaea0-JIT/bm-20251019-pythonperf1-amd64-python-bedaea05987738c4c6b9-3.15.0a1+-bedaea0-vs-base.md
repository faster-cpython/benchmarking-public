# Results vs. base

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.025x faster
- HPT reliability: 82.28%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.58 sec                                                                                                               | 1.61 sec: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|--------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets | 147 ms                                                                                                                 | 143 ms: 1.03x faster                                                                                                       |
| coroutines         | 14.4 ms                                                                                                                | 14.2 ms: 1.02x faster                                                                                                      |
| async_generators   | 234 ms                                                                                                                 | 248 ms: 1.06x slower                                                                                                       |
| asyncio_tcp_ssl    | 1.25 sec                                                                                                               | 1.41 sec: 1.12x slower                                                                                                     |
| asyncio_tcp        | 387 ms                                                                                                                 | 496 ms: 1.28x slower                                                                                                       |
| Geometric mean     | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (8): async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 62.9 ms                                                                                                                | 54.6 ms: 1.15x faster                                                                                                      |
| float          | 44.4 ms                                                                                                                | 40.8 ms: 1.09x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.08x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                                                                 | 114 ms: 1.07x faster                                                                                                       |
| regex_v8       | 14.0 ms                                                                                                                | 13.4 ms: 1.05x faster                                                                                                      |
| regex_effbot   | 1.56 ms                                                                                                                | 1.52 ms: 1.03x faster                                                                                                      |
| regex_compile  | 78.8 ms                                                                                                                | 77.6 ms: 1.02x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                                                                                 | 104 us: 1.28x faster                                                                                                       |
| tomli_loads          | 1.32 sec                                                                                                               | 1.09 sec: 1.21x faster                                                                                                     |
| xml_etree_generate   | 55.6 ms                                                                                                                | 49.5 ms: 1.12x faster                                                                                                      |
| xml_etree_process    | 39.0 ms                                                                                                                | 35.6 ms: 1.10x faster                                                                                                      |
| pickle               | 7.76 us                                                                                                                | 7.34 us: 1.06x faster                                                                                                      |
| pickle_pure_python   | 206 us                                                                                                                 | 198 us: 1.04x faster                                                                                                       |
| unpickle_list        | 2.89 us                                                                                                                | 2.79 us: 1.04x faster                                                                                                      |
| xml_etree_iterparse  | 61.6 ms                                                                                                                | 60.1 ms: 1.03x faster                                                                                                      |
| xml_etree_parse      | 86.3 ms                                                                                                                | 84.9 ms: 1.02x faster                                                                                                      |
| pickle_list          | 3.20 us                                                                                                                | 3.18 us: 1.01x faster                                                                                                      |
| json_dumps           | 5.44 ms                                                                                                                | 5.51 ms: 1.01x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.06x faster                                                                                                               |

Benchmark hidden because not significant (3): json_loads, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 26.1 ms                                                                                                                | 25.2 ms: 1.03x faster                                                                                                      |
| python_startup_no_site | 19.2 ms                                                                                                                | 18.8 ms: 1.02x faster                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.63 ms                                                                                                                | 5.32 ms: 1.25x faster                                                                                                      |
| django_template | 23.0 ms                                                                                                                | 23.8 ms: 1.03x slower                                                                                                      |
| genshi_text     | 15.1 ms                                                                                                                | 15.7 ms: 1.04x slower                                                                                                      |
| genshi_xml      | 33.4 ms                                                                                                                | 34.8 ms: 1.04x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python     | 133 us                                                                                                                 | 104 us: 1.28x faster                                                                                                       |
| scimark_fft              | 168 ms                                                                                                                 | 134 ms: 1.25x faster                                                                                                       |
| mako                     | 6.63 ms                                                                                                                | 5.32 ms: 1.25x faster                                                                                                      |
| fannkuch                 | 258 ms                                                                                                                 | 211 ms: 1.22x faster                                                                                                       |
| tomli_loads              | 1.32 sec                                                                                                               | 1.09 sec: 1.21x faster                                                                                                     |
| unpack_sequence          | 40.2 ns                                                                                                                | 34.2 ns: 1.17x faster                                                                                                      |
| pprint_safe_repr         | 489 ms                                                                                                                 | 416 ms: 1.17x faster                                                                                                       |
| pprint_pformat           | 995 ms                                                                                                                 | 850 ms: 1.17x faster                                                                                                       |
| nbody                    | 62.9 ms                                                                                                                | 54.6 ms: 1.15x faster                                                                                                      |
| bpe_tokeniser            | 2.91 sec                                                                                                               | 2.54 sec: 1.15x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.44 ms                                                                                                                | 2.16 ms: 1.13x faster                                                                                                      |
| xml_etree_generate       | 55.6 ms                                                                                                                | 49.5 ms: 1.12x faster                                                                                                      |
| xml_etree_process        | 39.0 ms                                                                                                                | 35.6 ms: 1.10x faster                                                                                                      |
| pyflate                  | 276 ms                                                                                                                 | 252 ms: 1.09x faster                                                                                                       |
| telco                    | 4.23 ms                                                                                                                | 3.88 ms: 1.09x faster                                                                                                      |
| float                    | 44.4 ms                                                                                                                | 40.8 ms: 1.09x faster                                                                                                      |
| regex_dna                | 122 ms                                                                                                                 | 114 ms: 1.07x faster                                                                                                       |
| pickle                   | 7.76 us                                                                                                                | 7.34 us: 1.06x faster                                                                                                      |
| sqlglot_v2_parse         | 799 us                                                                                                                 | 759 us: 1.05x faster                                                                                                       |
| sqlglot_v2_transpile     | 1.02 ms                                                                                                                | 966 us: 1.05x faster                                                                                                       |
| regex_v8                 | 14.0 ms                                                                                                                | 13.4 ms: 1.05x faster                                                                                                      |
| k_core                   | 1.66 sec                                                                                                               | 1.59 sec: 1.05x faster                                                                                                     |
| connected_components     | 327 ms                                                                                                                 | 313 ms: 1.05x faster                                                                                                       |
| mdp                      | 813 ms                                                                                                                 | 781 ms: 1.04x faster                                                                                                       |
| pickle_pure_python       | 206 us                                                                                                                 | 198 us: 1.04x faster                                                                                                       |
| unpickle_list            | 2.89 us                                                                                                                | 2.79 us: 1.04x faster                                                                                                      |
| typing_runtime_protocols | 104 us                                                                                                                 | 101 us: 1.04x faster                                                                                                       |
| shortest_path            | 355 ms                                                                                                                 | 343 ms: 1.04x faster                                                                                                       |
| pycparser                | 693 ms                                                                                                                 | 670 ms: 1.04x faster                                                                                                       |
| crypto_pyaes             | 46.4 ms                                                                                                                | 44.8 ms: 1.03x faster                                                                                                      |
| python_startup           | 26.1 ms                                                                                                                | 25.2 ms: 1.03x faster                                                                                                      |
| asyncio_websockets       | 147 ms                                                                                                                 | 143 ms: 1.03x faster                                                                                                       |
| regex_effbot             | 1.56 ms                                                                                                                | 1.52 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse      | 61.6 ms                                                                                                                | 60.1 ms: 1.03x faster                                                                                                      |
| json                     | 2.89 ms                                                                                                                | 2.83 ms: 1.02x faster                                                                                                      |
| python_startup_no_site   | 19.2 ms                                                                                                                | 18.8 ms: 1.02x faster                                                                                                      |
| create_gc_cycles         | 1.27 ms                                                                                                                | 1.25 ms: 1.02x faster                                                                                                      |
| coroutines               | 14.4 ms                                                                                                                | 14.2 ms: 1.02x faster                                                                                                      |
| xml_etree_parse          | 86.3 ms                                                                                                                | 84.9 ms: 1.02x faster                                                                                                      |
| regex_compile            | 78.8 ms                                                                                                                | 77.6 ms: 1.02x faster                                                                                                      |
| comprehensions           | 10.8 us                                                                                                                | 10.7 us: 1.01x faster                                                                                                      |
| sqlite_synth             | 1.54 us                                                                                                                | 1.53 us: 1.01x faster                                                                                                      |
| pickle_list              | 3.20 us                                                                                                                | 3.18 us: 1.01x faster                                                                                                      |
| deltablue                | 2.16 ms                                                                                                                | 2.18 ms: 1.01x slower                                                                                                      |
| scimark_sor              | 75.9 ms                                                                                                                | 76.7 ms: 1.01x slower                                                                                                      |
| json_dumps               | 5.44 ms                                                                                                                | 5.51 ms: 1.01x slower                                                                                                      |
| gc_traversal             | 2.06 ms                                                                                                                | 2.09 ms: 1.01x slower                                                                                                      |
| meteor_contest           | 70.7 ms                                                                                                                | 71.8 ms: 1.02x slower                                                                                                      |
| docutils                 | 1.58 sec                                                                                                               | 1.61 sec: 1.02x slower                                                                                                     |
| richards                 | 26.6 ms                                                                                                                | 27.0 ms: 1.02x slower                                                                                                      |
| logging_silent           | 55.3 ns                                                                                                                | 56.4 ns: 1.02x slower                                                                                                      |
| hexiom                   | 3.99 ms                                                                                                                | 4.07 ms: 1.02x slower                                                                                                      |
| bench_thread_pool        | 824 us                                                                                                                 | 841 us: 1.02x slower                                                                                                       |
| pathlib                  | 28.5 ms                                                                                                                | 29.2 ms: 1.02x slower                                                                                                      |
| deepcopy_reduce          | 1.75 us                                                                                                                | 1.80 us: 1.03x slower                                                                                                      |
| sqlglot_v2_optimize      | 33.8 ms                                                                                                                | 34.7 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_normalize     | 68.5 ms                                                                                                                | 70.3 ms: 1.03x slower                                                                                                      |
| many_optionals           | 560 us                                                                                                                 | 575 us: 1.03x slower                                                                                                       |
| logging_format           | 6.39 us                                                                                                                | 6.58 us: 1.03x slower                                                                                                      |
| spectral_norm            | 61.1 ms                                                                                                                | 63.0 ms: 1.03x slower                                                                                                      |
| sympy_integrate          | 12.1 ms                                                                                                                | 12.5 ms: 1.03x slower                                                                                                      |
| django_template          | 23.0 ms                                                                                                                | 23.8 ms: 1.03x slower                                                                                                      |
| logging_simple           | 5.91 us                                                                                                                | 6.13 us: 1.04x slower                                                                                                      |
| scimark_monte_carlo      | 39.7 ms                                                                                                                | 41.3 ms: 1.04x slower                                                                                                      |
| genshi_text              | 15.1 ms                                                                                                                | 15.7 ms: 1.04x slower                                                                                                      |
| genshi_xml               | 33.4 ms                                                                                                                | 34.8 ms: 1.04x slower                                                                                                      |
| sympy_expand             | 276 ms                                                                                                                 | 289 ms: 1.05x slower                                                                                                       |
| chaos                    | 38.9 ms                                                                                                                | 41.1 ms: 1.06x slower                                                                                                      |
| async_generators         | 234 ms                                                                                                                 | 248 ms: 1.06x slower                                                                                                       |
| scimark_lu               | 54.6 ms                                                                                                                | 57.8 ms: 1.06x slower                                                                                                      |
| coverage                 | 48.4 ms                                                                                                                | 51.3 ms: 1.06x slower                                                                                                      |
| asyncio_tcp_ssl          | 1.25 sec                                                                                                               | 1.41 sec: 1.12x slower                                                                                                     |
| asyncio_tcp              | 387 ms                                                                                                                 | 496 ms: 1.28x slower                                                                                                       |
| Geometric mean           | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (29): async_tree_none, json_loads, async_tree_none_tg, deepcopy_memo, async_tree_memoization, async_tree_io_tg, async_tree_io, nqueens, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, bench_mp_pool, deepcopy, pickle_dict, sphinx, thrift, 2to3, pidigits, generators, pylint, html5lib, async_tree_memoization_tg, richards_super, sympy_sum, unpickle, dulwich_log, subparsers, raytrace, sympy_str, go

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 82.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown