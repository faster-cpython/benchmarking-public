# Results vs. 3.10.4

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.323x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.57x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.51x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.43x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 40.2 ms: 1.53x faster                                                      |
| nbody          | 71.3 ms                                                     | 54.6 ms: 1.31x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.7 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.72x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.44 ms: 1.68x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.4 ms: 1.26x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.7 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.71 us: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| pickle               | 6.85 us                                                     | 7.73 us: 1.13x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.8 us: 1.15x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.25 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.36 ms: 1.69x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.24x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.57x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.4 ms: 2.57x faster                                                      |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.51x faster                                                       |
| mdp                      | 1.78 sec                                                    | 807 ms: 2.21x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| go                       | 139 ms                                                      | 76.5 ms: 1.82x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.5 ns: 1.74x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.72x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.71x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.36 ms: 1.69x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.44 ms: 1.68x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.4 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.66x faster                                                      |
| pyflate                  | 409 ms                                                      | 251 ms: 1.63x faster                                                       |
| raytrace                 | 273 ms                                                      | 176 ms: 1.56x faster                                                       |
| deepcopy                 | 255 us                                                      | 165 us: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| float                    | 61.7 ms                                                     | 40.2 ms: 1.53x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.53x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.1 ms: 1.48x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.47x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 506 ms: 1.45x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.1 ms: 1.43x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 864 ms: 1.41x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.08 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.3 ms: 1.38x faster                                                      |
| scimark_sor              | 106 ms                                                      | 78.2 ms: 1.36x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 439 ms: 1.35x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.7 ms: 1.35x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                       |
| pycparser                | 930 ms                                                      | 712 ms: 1.31x faster                                                       |
| nbody                    | 71.3 ms                                                     | 54.6 ms: 1.31x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.27x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.4 ms: 1.26x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.7 ms: 1.24x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.4 ms: 1.24x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 88.1 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                       |
| fannkuch                 | 256 ms                                                      | 216 ms: 1.18x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 34.5 ns: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 873 us: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.3 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.7 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.71 us: 1.04x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.54 us: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.06 us: 1.03x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.2 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.08 ms: 1.04x slower                                                      |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.73 us: 1.13x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.8 us: 1.15x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.25 us: 1.18x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 91.4 ms: 1.47x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.28 ms: 1.59x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.29x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.323x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown