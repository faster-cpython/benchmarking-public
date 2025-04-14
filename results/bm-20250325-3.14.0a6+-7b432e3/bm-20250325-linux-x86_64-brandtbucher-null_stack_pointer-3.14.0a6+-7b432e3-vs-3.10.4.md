# Results vs. 3.10.4

- fork: brandtbucher
- ref: null_stack_pointer
- machine: linux-x86_64
- commit hash: 7b432e3
- commit date: 2025-03-25
- overall geometric mean: 1.443x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                       |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                     |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 614 ms: 2.88x faster                                                       |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.08x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.9 ms: 1.70x faster                                                      |
| nbody          | 154 ms                                                 | 96.6 ms: 1.59x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.40x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                      |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.34x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.18x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                      |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                      |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 48.4 ms: 1.37x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 614 ms: 2.88x faster                                                       |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                      |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.09 ms: 2.56x faster                                                      |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.08x faster                                                       |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                      |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                      |
| logging_silent           | 190 ns                                                 | 97.8 ns: 1.94x faster                                                      |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                       |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                      |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                       |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                      |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                      |
| spectral_norm            | 170 ms                                                 | 98.6 ms: 1.72x faster                                                      |
| float                    | 117 ms                                                 | 68.9 ms: 1.70x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.69x faster                                                      |
| pyflate                  | 716 ms                                                 | 429 ms: 1.67x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                      |
| nbody                    | 154 ms                                                 | 96.6 ms: 1.59x faster                                                      |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                       |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                       |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                      |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 58.3 ms: 1.45x faster                                                      |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                       |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 48.4 ms: 1.37x faster                                                      |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.34x faster                                                      |
| scimark_fft              | 466 ms                                                 | 348 ms: 1.34x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                      |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                       |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                       |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                     |
| fannkuch                 | 532 ms                                                 | 425 ms: 1.25x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.18x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                       |
| async_generators         | 444 ms                                                 | 394 ms: 1.13x faster                                                       |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                       |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                      |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                      |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                      |
| coverage                 | 79.4 ms                                                | 93.3 ms: 1.17x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 83.2 ms: 3.47x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                               |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250325-3.14.0a6+-7b432e3/bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.443x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x