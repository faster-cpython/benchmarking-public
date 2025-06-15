# Results vs. 3.10.4

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: windows-amd64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.152x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.51x faster                                                       |
| async_tree_none         | 435 ms                                                      | 179 ms: 2.44x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.39x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.2 ms: 1.32x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.3 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.7 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.51x faster                                                       |
| async_tree_none          | 435 ms                                                      | 179 ms: 2.44x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 808 ms: 2.20x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.86x faster                                                      |
| go                       | 139 ms                                                      | 77.5 ms: 1.79x faster                                                      |
| pylint                   | 350 ms                                                      | 201 ms: 1.75x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.4 us: 1.56x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                       |
| raytrace                 | 273 ms                                                      | 184 ms: 1.49x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 59.5 ms: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.4 ms: 1.42x faster                                                      |
| pyflate                  | 409 ms                                                      | 289 ms: 1.41x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.1 ms: 1.40x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.15 ms: 1.38x faster                                                      |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.0 ms: 1.33x faster                                                      |
| regex_compile            | 106 ms                                                      | 80.2 ms: 1.32x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 59.2 ms: 1.31x faster                                                      |
| pycparser                | 930 ms                                                      | 724 ms: 1.29x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.3 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 61.2 ms: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.3 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 548 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.7 ms: 1.04x faster                                                      |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                       |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                      |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.7 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.91 us: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.46 us: 1.04x slower                                                      |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 321 ns: 3.39x slower                                                       |
| coverage                 | 39.0 ms                                                     | 296 ms: 7.59x slower                                                       |
| thrift                   | 617 us                                                      | 98.3 ms: 159.21x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.152x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown