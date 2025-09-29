# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.312x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.14x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.1 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 380 ms: 2.92x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.48x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 63.0 ms: 1.13x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.9 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.36 ms: 1.71x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.55 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.85 us: 1.05x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.5 us: 1.13x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.21 us: 1.17x slower                                                      |
| pickle               | 6.85 us                                                     | 8.08 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.41 ms: 1.41x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 380 ms: 2.92x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.0 ms: 2.61x faster                                                      |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| mdp                      | 1.78 sec                                                    | 796 ms: 2.24x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.13 ms: 1.97x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 377 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| go                       | 139 ms                                                      | 75.2 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 191 ms: 1.84x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.4 us: 1.76x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.0 ms: 1.74x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.36 ms: 1.71x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.25 sec: 1.69x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 56.5 ns: 1.67x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.5 ms: 1.60x faster                                                      |
| deepcopy                 | 255 us                                                      | 163 us: 1.57x faster                                                       |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.9 ms: 1.51x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 57.1 ms: 1.50x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                      |
| pyflate                  | 409 ms                                                      | 274 ms: 1.50x faster                                                       |
| scimark_sor              | 106 ms                                                      | 72.9 ms: 1.46x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.99 ms: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.41 ms: 1.41x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.1 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.9 ms: 1.36x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                                       |
| pycparser                | 930 ms                                                      | 694 ms: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.2 ms: 1.32x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 38.8 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| sympy_sum                | 107 ms                                                      | 85.1 ms: 1.26x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 972 ms: 1.25x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.77 us: 1.25x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 476 ms: 1.24x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.2 ms: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 497 us: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 829 us: 1.16x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 34.4 ns: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| 2to3                     | 246 ms                                                      | 215 ms: 1.14x faster                                                       |
| nbody                    | 71.3 ms                                                     | 63.0 ms: 1.13x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                      |
| sympy_expand             | 314 ms                                                      | 282 ms: 1.12x faster                                                       |
| scimark_fft              | 187 ms                                                      | 170 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.50 ms: 1.09x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                      |
| json                     | 3.14 ms                                                     | 2.89 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.0 ms: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.33 us: 1.07x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.84 us: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.55 us: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| fannkuch                 | 256 ms                                                      | 259 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.13 ms: 1.05x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.85 us: 1.05x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.5 us: 1.13x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.21 us: 1.17x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.08 us: 1.18x slower                                                      |
| python_startup           | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.9 ms: 1.25x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 89.4 ms: 1.44x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.49x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.312x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown