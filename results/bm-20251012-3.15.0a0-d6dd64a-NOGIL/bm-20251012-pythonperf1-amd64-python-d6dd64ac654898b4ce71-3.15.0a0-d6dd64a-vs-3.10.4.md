# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.193x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.86 sec: 1.49x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 339 ms: 3.27x faster                                                       |
| async_tree_none         | 435 ms                                                      | 165 ms: 2.64x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 211 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 323 ms: 1.97x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.55x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.2 ms: 1.37x faster                                                      |
| pidigits       | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| nbody          | 71.3 ms                                                     | 78.2 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| regex_compile  | 106 ms                                                      | 89.2 ms: 1.19x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.04 ms: 1.52x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 146 us: 1.26x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 222 us: 1.21x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.3 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.3 ms: 1.08x faster                                                      |
| unpickle             | 9.09 us                                                     | 9.61 us: 1.06x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 60.6 ms: 1.09x slower                                                      |
| pickle               | 6.85 us                                                     | 7.82 us: 1.14x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.1 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.3 us: 1.18x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.23 us: 1.19x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.28 sec: 1.36x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                      |
| mako            | 9.03 ms                                                     | 10.1 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 339 ms: 3.27x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 127 us: 2.65x faster                                                       |
| async_tree_none          | 435 ms                                                      | 165 ms: 2.64x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.9 ms: 2.62x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 211 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 323 ms: 1.97x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.32 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.05 sec: 1.69x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 456 ms: 1.60x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 59.8 ns: 1.58x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.4 us: 1.56x faster                                                      |
| go                       | 139 ms                                                      | 90.0 ms: 1.54x faster                                                      |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.54x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.04 ms: 1.52x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.8 ms: 1.42x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.38 us: 1.39x faster                                                      |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                       |
| pyflate                  | 409 ms                                                      | 296 ms: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 45.2 ms: 1.37x faster                                                      |
| chaos                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 687 ms: 1.35x faster                                                       |
| richards                 | 42.4 ms                                                     | 31.4 ms: 1.35x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 64.4 ms: 1.33x faster                                                      |
| raytrace                 | 273 ms                                                      | 206 ms: 1.33x faster                                                       |
| scimark_sor              | 106 ms                                                      | 80.9 ms: 1.31x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.40 ms: 1.30x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.28x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 146 us: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.7 ms: 1.24x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 222 us: 1.21x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.2 ms: 1.19x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.9 ms: 1.17x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.22 ms: 1.16x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 67.7 ms: 1.14x faster                                                      |
| sympy_sum                | 107 ms                                                      | 93.9 ms: 1.14x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 35.1 ns: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.3 ms: 1.11x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 56.3 ms: 1.11x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 533 ms: 1.11x faster                                                       |
| thrift                   | 617 us                                                      | 557 us: 1.11x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.99 us: 1.11x faster                                                      |
| pidigits                 | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.3 ms: 1.08x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 181 ms: 1.07x faster                                                       |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.97 us: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.54 us: 1.05x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.61 us: 1.06x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.02 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.90 ms: 1.06x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 71.0 ms: 1.07x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 60.6 ms: 1.09x slower                                                      |
| nbody                    | 71.3 ms                                                     | 78.2 ms: 1.10x slower                                                      |
| mako                     | 9.03 ms                                                     | 10.1 ms: 1.12x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 85.4 ms: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.82 us: 1.14x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.1 us: 1.15x slower                                                      |
| fannkuch                 | 256 ms                                                      | 300 ms: 1.17x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.3 us: 1.18x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.23 us: 1.19x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 74.5 ms: 1.20x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.02 ms: 1.28x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.59 sec: 1.30x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.28 sec: 1.36x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.86 sec: 1.49x slower                                                     |
| coverage                 | 39.0 ms                                                     | 68.2 ms: 1.75x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (4): regex_effbot, xml_etree_process, scimark_fft, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.193x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown