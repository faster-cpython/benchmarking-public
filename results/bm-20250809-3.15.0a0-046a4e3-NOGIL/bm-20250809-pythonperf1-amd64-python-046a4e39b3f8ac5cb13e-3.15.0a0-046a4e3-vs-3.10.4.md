# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.145x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.79 sec: 1.45x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 352 ms: 3.15x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.51x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 325 ms: 1.97x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.51x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                      |
| pidigits       | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| nbody          | 71.3 ms                                                     | 85.0 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| regex_compile  | 106 ms                                                      | 93.6 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.89 ms: 1.56x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 160 us: 1.15x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 237 us: 1.14x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 57.4 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.93 us: 1.06x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.6 us: 1.11x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.1 us: 1.11x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 61.9 ms: 1.11x slower                                                      |
| pickle               | 6.85 us                                                     | 7.72 us: 1.13x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.07 us: 1.13x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.8 us: 1.16x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.67 sec: 1.60x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| mako            | 9.03 ms                                                     | 9.93 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 352 ms: 3.15x faster                                                       |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 134 us: 2.51x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.51x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 36.1 ms: 2.10x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 325 ms: 1.97x faster                                                       |
| pylint                   | 350 ms                                                      | 201 ms: 1.75x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.45 ms: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.89 ms: 1.56x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.15 sec: 1.55x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 61.4 ns: 1.54x faster                                                      |
| go                       | 139 ms                                                      | 92.3 ms: 1.51x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.36 us: 1.41x faster                                                      |
| generators               | 32.4 ms                                                     | 23.6 ms: 1.37x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                      |
| float                    | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 547 ms: 1.34x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.1 ms: 1.34x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.5 us: 1.34x faster                                                      |
| chaos                    | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                      |
| raytrace                 | 273 ms                                                      | 208 ms: 1.31x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 65.8 ms: 1.30x faster                                                      |
| pyflate                  | 409 ms                                                      | 321 ms: 1.27x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.5 ms: 1.27x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                       |
| deepcopy                 | 255 us                                                      | 207 us: 1.23x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.74 ms: 1.21x faster                                                      |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.9 ms: 1.20x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| scimark_sor              | 106 ms                                                      | 90.3 ms: 1.18x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.20 ms: 1.17x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 160 us: 1.15x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 237 us: 1.14x faster                                                       |
| regex_compile            | 106 ms                                                      | 93.6 ms: 1.13x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 57.4 ms: 1.13x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.7 ms: 1.13x faster                                                      |
| sympy_sum                | 107 ms                                                      | 95.8 ms: 1.12x faster                                                      |
| pidigits                 | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 57.1 ms: 1.09x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| thrift                   | 617 us                                                      | 567 us: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| coroutines               | 16.0 ms                                                     | 15.3 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 567 ms: 1.04x faster                                                       |
| sympy_str                | 194 ms                                                      | 187 ms: 1.04x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.14 us: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.02x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 39.1 ns: 1.01x faster                                                      |
| sympy_expand             | 314 ms                                                      | 325 ms: 1.03x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.14 us: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.93 us: 1.06x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.65 us: 1.07x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.93 ms: 1.10x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.6 us: 1.11x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.1 us: 1.11x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 61.9 ms: 1.11x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 74.7 ms: 1.12x slower                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.37 sec: 1.12x slower                                                     |
| meteor_contest           | 75.9 ms                                                     | 85.6 ms: 1.13x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.72 us: 1.13x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.07 us: 1.13x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.09 ms: 1.13x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.09 ms: 1.14x slower                                                      |
| async_generators         | 222 ms                                                      | 256 ms: 1.15x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.8 us: 1.16x slower                                                      |
| scimark_fft              | 187 ms                                                      | 217 ms: 1.16x slower                                                       |
| nbody                    | 71.3 ms                                                     | 85.0 ms: 1.19x slower                                                      |
| fannkuch                 | 256 ms                                                      | 316 ms: 1.24x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 79.2 ms: 1.28x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.02 ms: 1.28x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.19 ms: 1.32x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.69 sec: 1.39x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.79 sec: 1.45x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.67 sec: 1.60x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.6 ms: 1.71x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_process, spectral_norm, genshi_xml, genshi_text
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.145x faster

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown