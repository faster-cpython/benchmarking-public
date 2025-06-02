# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.141x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 289 ms: 1.20x faster                                                  |
| docutils       | 3.30 sec                                               | 2.84 sec: 1.16x faster                                                |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 662 ms: 2.67x faster                                                  |
| async_tree_none         | 728 ms                                                 | 291 ms: 2.50x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 350 ms: 2.48x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 607 ms: 1.67x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 75.1 ms: 1.56x faster                                                 |
| nbody          | 154 ms                                                 | 109 ms: 1.41x faster                                                  |
| pidigits       | 191 ms                                                 | 202 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.31x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.00 ms: 1.21x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.25 sec: 1.39x faster                                                |
| unpickle_pure_python | 331 us                                                 | 255 us: 1.30x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 380 us: 1.27x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 73.6 ms: 1.08x faster                                                 |
| json_dumps           | 14.2 ms                                                | 13.3 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                  |
| unpickle_list        | 5.20 us                                                | 5.59 us: 1.07x slower                                                 |
| xml_etree_generate   | 99.4 ms                                                | 107 ms: 1.08x slower                                                  |
| json_loads           | 31.2 us                                                | 33.9 us: 1.09x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.85 us: 1.15x slower                                                 |
| pickle_dict          | 29.6 us                                                | 36.2 us: 1.22x slower                                                 |
| unpickle             | 14.4 us                                                | 18.9 us: 1.31x slower                                                 |
| pickle               | 10.7 us                                                | 15.0 us: 1.41x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.42 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                 |
| django_template | 48.2 ms                                                | 40.3 ms: 1.19x faster                                                 |
| mako            | 16.3 ms                                                | 13.7 ms: 1.19x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.5 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 195 us: 2.80x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 662 ms: 2.67x faster                                                  |
| async_tree_none          | 728 ms                                                 | 291 ms: 2.50x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 350 ms: 2.48x faster                                                  |
| generators               | 80.1 ms                                                | 32.4 ms: 2.47x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.86 ms: 2.05x faster                                                 |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.47 sec: 1.93x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.91x faster                                                  |
| pylint                   | 551 ms                                                 | 310 ms: 1.78x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 34.0 us: 1.72x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 607 ms: 1.67x faster                                                  |
| chaos                    | 115 ms                                                 | 69.9 ms: 1.65x faster                                                 |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.62x faster                                                  |
| raytrace                 | 507 ms                                                 | 319 ms: 1.59x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.66 ms: 1.56x faster                                                 |
| float                    | 117 ms                                                 | 75.1 ms: 1.56x faster                                                 |
| deepcopy                 | 479 us                                                 | 310 us: 1.54x faster                                                  |
| richards_super           | 94.7 ms                                                | 61.5 ms: 1.54x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 78.2 ms: 1.51x faster                                                 |
| comprehensions           | 28.8 us                                                | 19.1 us: 1.51x faster                                                 |
| pyflate                  | 716 ms                                                 | 476 ms: 1.51x faster                                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 87.1 ms: 1.47x faster                                                 |
| richards                 | 79.3 ms                                                | 54.3 ms: 1.46x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.42x faster                                                |
| nbody                    | 154 ms                                                 | 109 ms: 1.41x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.25 sec: 1.39x faster                                                |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.0 ms: 1.32x faster                                                 |
| scimark_lu               | 176 ms                                                 | 134 ms: 1.31x faster                                                  |
| regex_compile            | 188 ms                                                 | 143 ms: 1.31x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 255 us: 1.30x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 380 us: 1.27x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.25 sec: 1.26x faster                                                |
| coroutines               | 35.1 ms                                                | 28.1 ms: 1.25x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.9 ms: 1.23x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.00 ms: 1.21x faster                                                 |
| 2to3                     | 348 ms                                                 | 289 ms: 1.20x faster                                                  |
| django_template          | 48.2 ms                                                | 40.3 ms: 1.19x faster                                                 |
| mako                     | 16.3 ms                                                | 13.7 ms: 1.19x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 50.5 ns: 1.19x faster                                                 |
| sympy_sum                | 196 ms                                                 | 166 ms: 1.18x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.84 sec: 1.16x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 57.5 ms: 1.15x faster                                                 |
| pathlib                  | 20.5 ms                                                | 18.2 ms: 1.13x faster                                                 |
| sympy_str                | 346 ms                                                 | 307 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.78 ms: 1.12x faster                                                 |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                  |
| scimark_fft              | 466 ms                                                 | 420 ms: 1.11x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| logging_simple           | 8.30 us                                                | 7.52 us: 1.10x faster                                                 |
| fannkuch                 | 532 ms                                                 | 491 ms: 1.08x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 73.6 ms: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 416 ms: 1.07x faster                                                  |
| nqueens                  | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| json_dumps               | 14.2 ms                                                | 13.3 ms: 1.06x faster                                                 |
| sympy_expand             | 566 ms                                                 | 534 ms: 1.06x faster                                                  |
| logging_format           | 9.09 us                                                | 8.58 us: 1.06x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 2.01 sec: 1.04x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 988 ms: 1.03x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 957 us: 1.03x faster                                                  |
| meteor_contest           | 120 ms                                                 | 116 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 3.17 us: 1.05x slower                                                 |
| pidigits                 | 191 ms                                                 | 202 ms: 1.06x slower                                                  |
| json                     | 5.69 ms                                                | 6.11 ms: 1.07x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.59 us: 1.07x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 107 ms: 1.08x slower                                                  |
| json_loads               | 31.2 us                                                | 33.9 us: 1.09x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.85 us: 1.15x slower                                                 |
| pickle_dict              | 29.6 us                                                | 36.2 us: 1.22x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.42 ms: 1.25x slower                                                 |
| telco                    | 7.27 ms                                                | 9.39 ms: 1.29x slower                                                 |
| unpickle                 | 14.4 us                                                | 18.9 us: 1.31x slower                                                 |
| pickle                   | 10.7 us                                                | 15.0 us: 1.41x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.16 ms: 1.42x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.63 ms: 1.62x slower                                                 |
| logging_silent           | 190 ns                                                 | 651 ns: 3.43x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 104 ms: 4.33x slower                                                  |
| coverage                 | 79.4 ms                                                | 514 ms: 6.48x slower                                                  |
| thrift                   | 1.07 ms                                                | 149 ms: 138.91x slower                                                |
| Geometric mean           | (ref)                                                  | 1.11x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.141x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.31x