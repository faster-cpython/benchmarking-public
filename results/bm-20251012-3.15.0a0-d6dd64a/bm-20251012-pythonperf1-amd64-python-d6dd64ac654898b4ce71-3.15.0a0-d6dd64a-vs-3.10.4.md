# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.293x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 384 ms: 2.89x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 202 ms: 2.60x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.2 ms: 1.36x faster                                                      |
| nbody          | 71.3 ms                                                     | 67.4 ms: 1.06x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.4 ms: 1.32x faster                                                      |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.35x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.54 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.95 us: 1.16x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.29 us: 1.19x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.5 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.67 ms: 1.35x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.31x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 384 ms: 2.89x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 202 ms: 2.60x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.1 ms: 2.60x faster                                                      |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| mdp                      | 1.78 sec                                                    | 790 ms: 2.25x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 372 ms: 1.97x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 192 ms: 1.83x faster                                                       |
| go                       | 139 ms                                                      | 76.8 ms: 1.81x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.24 sec: 1.70x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 56.1 ns: 1.69x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.3 ms: 1.67x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.4 us: 1.65x faster                                                      |
| deepcopy                 | 255 us                                                      | 164 us: 1.56x faster                                                       |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.7 ms: 1.46x faster                                                      |
| pyflate                  | 409 ms                                                      | 283 ms: 1.45x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.1 ms: 1.39x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.14 ms: 1.39x faster                                                      |
| scimark_sor              | 106 ms                                                      | 77.1 ms: 1.38x faster                                                      |
| float                    | 61.7 ms                                                     | 45.2 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| pycparser                | 930 ms                                                      | 687 ms: 1.35x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.35x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.67 ms: 1.35x faster                                                      |
| regex_compile            | 106 ms                                                      | 80.4 ms: 1.32x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 38.5 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 48.3 ms: 1.29x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                       |
| sympy_sum                | 107 ms                                                      | 85.2 ms: 1.26x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.79 us: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| thrift                   | 617 us                                                      | 501 us: 1.23x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                                     |
| django_template          | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 490 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 66.6 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 839 us: 1.14x faster                                                       |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                      |
| sympy_expand             | 314 ms                                                      | 281 ms: 1.12x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 35.7 ns: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.09x faster                                                      |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.54 us: 1.06x faster                                                      |
| nbody                    | 71.3 ms                                                     | 67.4 ms: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.42 us: 1.05x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 63.4 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.3 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.96 us: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.20 ms: 1.07x slower                                                      |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.95 us: 1.16x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.29 us: 1.19x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.5 us: 1.20x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.07 ms: 1.47x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.57x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.293x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown