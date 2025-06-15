# Results vs. 3.10.4

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.159x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 288 ms: 1.17x slower                                                       |
| docutils       | 1.92 sec                                                    | 2.11 sec: 1.10x slower                                                     |
| html5lib       | 51.0 ms                                                     | 51.9 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 531 ms: 2.09x faster                                                       |
| async_tree_none         | 435 ms                                                      | 232 ms: 1.87x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 285 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 432 ms: 1.48x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.81x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 56.2 ms: 1.27x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| float          | 61.7 ms                                                     | 78.7 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.74 ms: 1.05x slower                                                      |
| regex_v8       | 15.4 ms                                                     | 16.6 ms: 1.07x slower                                                      |
| regex_compile  | 106 ms                                                      | 120 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.56 sec: 1.07x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 8.63 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 105 ms: 1.09x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.08 us: 1.14x slower                                                      |
| xml_etree_process    | 44.5 ms                                                     | 52.1 ms: 1.17x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 329 us: 1.22x slower                                                       |
| unpickle             | 9.09 us                                                     | 11.6 us: 1.27x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 71.8 ms: 1.29x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 22.6 us: 1.32x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 87.8 ms: 1.35x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.93 us: 1.43x slower                                                      |
| pickle               | 6.85 us                                                     | 9.86 us: 1.44x slower                                                      |
| json_loads           | 14.0 us                                                     | 20.9 us: 1.49x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.9 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.2 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.25 ms: 1.25x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 50.7 ms: 1.24x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 24.7 ms: 1.25x slower                                                      |
| django_template | 28.9 ms                                                     | 38.0 ms: 1.31x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 144 us: 2.33x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 34.8 ms: 2.17x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 531 ms: 2.09x faster                                                       |
| async_tree_none          | 435 ms                                                      | 232 ms: 1.87x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 285 ms: 1.84x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.19 sec: 1.49x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 432 ms: 1.48x faster                                                       |
| pylint                   | 350 ms                                                      | 250 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.40x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 569 ms: 1.29x faster                                                       |
| nbody                    | 71.3 ms                                                     | 56.2 ms: 1.27x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.25 ms: 1.25x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.73 us: 1.10x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.56 sec: 1.07x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 8.63 ms: 1.06x faster                                                      |
| pyflate                  | 409 ms                                                      | 387 ms: 1.06x faster                                                       |
| comprehensions           | 16.5 us                                                     | 15.8 us: 1.05x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| go                       | 139 ms                                                      | 137 ms: 1.01x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 62.0 ms: 1.01x faster                                                      |
| scimark_fft              | 187 ms                                                      | 189 ms: 1.01x slower                                                       |
| html5lib                 | 51.0 ms                                                     | 51.9 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.80 ms: 1.03x slower                                                      |
| dulwich_log              | 50.5 ms                                                     | 52.2 ms: 1.04x slower                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.74 ms: 1.05x slower                                                      |
| deepcopy                 | 255 us                                                      | 271 us: 1.06x slower                                                       |
| chaos                    | 61.7 ms                                                     | 66.0 ms: 1.07x slower                                                      |
| sympy_sum                | 107 ms                                                      | 115 ms: 1.07x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.6 ms: 1.07x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 81.6 ms: 1.07x slower                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 105 ms: 1.09x slower                                                       |
| deltablue                | 4.19 ms                                                     | 4.57 ms: 1.09x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.11 sec: 1.10x slower                                                     |
| sympy_integrate          | 15.3 ms                                                     | 17.0 ms: 1.11x slower                                                      |
| fannkuch                 | 256 ms                                                      | 284 ms: 1.11x slower                                                       |
| richards_super           | 52.2 ms                                                     | 58.5 ms: 1.12x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.37 sec: 1.12x slower                                                     |
| raytrace                 | 273 ms                                                      | 307 ms: 1.12x slower                                                       |
| regex_compile            | 106 ms                                                      | 120 ms: 1.13x slower                                                       |
| pprint_safe_repr         | 592 ms                                                      | 670 ms: 1.13x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.08 us: 1.14x slower                                                      |
| generators               | 32.4 ms                                                     | 37.3 ms: 1.15x slower                                                      |
| 2to3                     | 246 ms                                                      | 288 ms: 1.17x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 52.1 ms: 1.17x slower                                                      |
| sympy_str                | 194 ms                                                      | 233 ms: 1.20x slower                                                       |
| richards                 | 42.4 ms                                                     | 51.7 ms: 1.22x slower                                                      |
| deepcopy_memo            | 28.8 us                                                     | 35.1 us: 1.22x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 329 us: 1.22x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 50.7 ms: 1.24x slower                                                      |
| genshi_text              | 19.8 ms                                                     | 24.7 ms: 1.25x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.77 us: 1.26x slower                                                      |
| scimark_sor              | 106 ms                                                      | 135 ms: 1.27x slower                                                       |
| json                     | 3.14 ms                                                     | 3.99 ms: 1.27x slower                                                      |
| unpickle                 | 9.09 us                                                     | 11.6 us: 1.27x slower                                                      |
| float                    | 61.7 ms                                                     | 78.7 ms: 1.28x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.9 ms: 1.29x slower                                                      |
| sympy_expand             | 314 ms                                                      | 404 ms: 1.29x slower                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 73.7 ms: 1.29x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 71.8 ms: 1.29x slower                                                      |
| django_template          | 28.9 ms                                                     | 38.0 ms: 1.31x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 22.6 us: 1.32x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.2 ms: 1.32x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.24 ms: 1.33x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 87.8 ms: 1.35x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 90.4 ms: 1.36x slower                                                      |
| hexiom                   | 5.74 ms                                                     | 7.80 ms: 1.36x slower                                                      |
| scimark_lu               | 85.8 ms                                                     | 122 ms: 1.42x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.93 us: 1.43x slower                                                      |
| pickle                   | 6.85 us                                                     | 9.86 us: 1.44x slower                                                      |
| logging_format           | 6.76 us                                                     | 10.1 us: 1.49x slower                                                      |
| json_loads               | 14.0 us                                                     | 20.9 us: 1.49x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 115 ms: 1.49x slower                                                       |
| logging_simple           | 6.22 us                                                     | 9.44 us: 1.52x slower                                                      |
| async_generators         | 222 ms                                                      | 355 ms: 1.60x slower                                                       |
| coroutines               | 16.0 ms                                                     | 25.7 ms: 1.61x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 105 ms: 1.69x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.48 ms: 1.86x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 77.6 ns: 1.96x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.85 ms: 2.02x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 501 ns: 5.30x slower                                                       |
| coverage                 | 39.0 ms                                                     | 473 ms: 12.13x slower                                                      |
| thrift                   | 617 us                                                      | 104 ms: 168.46x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.21x slower                                                               |

Benchmark hidden because not significant (2): pycparser, bench_thread_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.159x slower

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown