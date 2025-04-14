# Results vs. 3.10.4

- fork: brandtbucher
- ref: null_stack_pointer
- machine: linux-x86_64
- commit hash: 7b432e3
- commit date: 2025-03-25
- overall geometric mean: 1.447x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                       |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                     |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                       |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.1 ms: 1.80x faster                                                      |
| nbody          | 154 ms                                                 | 88.1 ms: 1.74x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.48x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                       |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.19x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                      |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.21x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 210 us: 1.58x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                                      |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                      |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                      |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                       |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                                      |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.02 ms: 2.62x faster                                                      |
| richards_super           | 94.7 ms                                                | 40.2 ms: 2.35x faster                                                      |
| richards                 | 79.3 ms                                                | 35.5 ms: 2.23x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                      |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                       |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                      |
| logging_silent           | 190 ns                                                 | 98.2 ns: 1.93x faster                                                      |
| go                       | 240 ms                                                 | 127 ms: 1.88x faster                                                       |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                       |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                       |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                       |
| spectral_norm            | 170 ms                                                 | 92.7 ms: 1.83x faster                                                      |
| float                    | 117 ms                                                 | 65.1 ms: 1.80x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                      |
| nbody                    | 154 ms                                                 | 88.1 ms: 1.74x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 77.9 ms: 1.64x faster                                                      |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 210 us: 1.58x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                      |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.55x faster                                                      |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.82 ms: 1.52x faster                                                      |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                      |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                       |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                      |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                      |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                       |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.41x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                      |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                                       |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                      |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 783 ms: 1.30x faster                                                       |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.62 sec: 1.29x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                       |
| fannkuch                 | 532 ms                                                 | 425 ms: 1.25x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                      |
| nqueens                  | 106 ms                                                 | 86.2 ms: 1.23x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.19x faster                                                      |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                       |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                       |
| async_generators         | 444 ms                                                 | 414 ms: 1.07x faster                                                       |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                      |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                       |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.84 ms: 1.34x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 83.1 ms: 3.46x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                               |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250325-3.14.0a6+-7b432e3-JIT/bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.447x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.29x