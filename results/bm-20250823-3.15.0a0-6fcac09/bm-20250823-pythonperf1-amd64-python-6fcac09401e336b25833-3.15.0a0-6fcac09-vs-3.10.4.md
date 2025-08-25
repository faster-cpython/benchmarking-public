# Results vs. 3.10.4

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.304x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.7 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 384 ms: 2.89x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 62.8 ms: 1.14x faster                                                      |
| pidigits       | 149 ms                                                      | 143 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.1 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.36 ms: 1.71x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.38x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.6 ms: 1.11x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.37 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.0 us: 1.16x slower                                                      |
| pickle               | 6.85 us                                                     | 8.21 us: 1.20x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.35 us: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.24x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 384 ms: 2.89x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.4 ms: 2.49x faster                                                      |
| mdp                      | 1.78 sec                                                    | 800 ms: 2.22x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 381 ms: 1.92x faster                                                       |
| pylint                   | 350 ms                                                      | 192 ms: 1.83x faster                                                       |
| go                       | 139 ms                                                      | 76.5 ms: 1.82x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.1 ms: 1.74x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.2 ns: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.36 ms: 1.71x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.24 sec: 1.70x faster                                                     |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.68x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.4 ms: 1.61x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.60x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 53.6 ms: 1.60x faster                                                      |
| raytrace                 | 273 ms                                                      | 172 ms: 1.59x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.1 ms: 1.47x faster                                                      |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                       |
| scimark_sor              | 106 ms                                                      | 73.5 ms: 1.44x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.04 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.38x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.1 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.7 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 706 ms: 1.32x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.0 ms: 1.26x faster                                                      |
| thrift                   | 617 us                                                      | 493 us: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.7 ms: 1.23x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 991 ms: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 485 ms: 1.22x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| sympy_str                | 194 ms                                                      | 167 ms: 1.17x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 34.5 ns: 1.15x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 840 us: 1.14x faster                                                       |
| nbody                    | 71.3 ms                                                     | 62.8 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| sympy_expand             | 314 ms                                                      | 278 ms: 1.13x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.6 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.48 ms: 1.10x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.0 ms: 1.09x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.37 us: 1.09x faster                                                      |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                                      |
| scimark_fft              | 187 ms                                                      | 176 ms: 1.07x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.9 ms: 1.06x faster                                                      |
| pidigits                 | 149 ms                                                      | 143 ms: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.53 us: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.06 us: 1.03x faster                                                      |
| async_generators         | 222 ms                                                      | 224 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.14 ms: 1.05x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.0 us: 1.16x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.21 us: 1.20x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.35 us: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.5 ms: 1.29x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.10 ms: 1.49x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 94.3 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.29 ms: 1.62x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_generate, fannkuch
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.304x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown