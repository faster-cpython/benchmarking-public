# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-x86_64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 587 ms: 3.01x faster                                                  |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.84x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 308 ms: 2.82x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.02x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.8 ms: 1.81x faster                                                 |
| float          | 117 ms                                                 | 67.4 ms: 1.74x faster                                                 |
| pidigits       | 191 ms                                                 | 203 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.44x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 123 ms: 1.53x faster                                                  |
| regex_dna      | 227 ms                                                 | 198 ms: 1.15x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 210 us: 1.57x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 88.0 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| unpickle_list        | 5.20 us                                                | 4.71 us: 1.10x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                 |
| unpickle             | 14.4 us                                                | 14.1 us: 1.02x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.7 us: 1.17x slower                                                 |
| pickle               | 10.7 us                                                | 13.3 us: 1.25x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                 |
| django_template | 48.2 ms                                                | 31.8 ms: 1.52x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.37x faster                                                 |
| mako            | 16.3 ms                                                | 12.1 ms: 1.35x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 587 ms: 3.01x faster                                                  |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                 |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.84x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 308 ms: 2.82x faster                                                  |
| deltablue                | 7.91 ms                                                | 2.95 ms: 2.68x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.34x faster                                                |
| go                       | 240 ms                                                 | 106 ms: 2.27x faster                                                  |
| chaos                    | 115 ms                                                 | 53.6 ms: 2.15x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                                 |
| scimark_sor              | 220 ms                                                 | 107 ms: 2.05x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.02x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.0 ms: 2.02x faster                                                 |
| raytrace                 | 507 ms                                                 | 254 ms: 2.00x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 59.2 ms: 2.00x faster                                                 |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                  |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                                 |
| deepcopy                 | 479 us                                                 | 245 us: 1.95x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 479 ms: 1.92x faster                                                  |
| hexiom                   | 10.4 ms                                                | 5.67 ms: 1.83x faster                                                 |
| nbody                    | 154 ms                                                 | 84.8 ms: 1.81x faster                                                 |
| spectral_norm            | 170 ms                                                 | 94.4 ms: 1.80x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 72.9 ms: 1.75x faster                                                 |
| float                    | 117 ms                                                 | 67.4 ms: 1.74x faster                                                 |
| pyflate                  | 716 ms                                                 | 420 ms: 1.70x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.55 us: 1.64x faster                                                 |
| scimark_lu               | 176 ms                                                 | 108 ms: 1.63x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 210 us: 1.57x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.57x faster                                                 |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                 |
| regex_compile            | 188 ms                                                 | 123 ms: 1.53x faster                                                  |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.52x faster                                                 |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.51x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.38 ms: 1.48x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 57.9 ms: 1.46x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 18.3 ms: 1.41x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.96 us: 1.39x faster                                                 |
| 2to3                     | 348 ms                                                 | 253 ms: 1.37x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.37x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                |
| sympy_sum                | 196 ms                                                 | 144 ms: 1.37x faster                                                  |
| logging_format           | 9.09 us                                                | 6.72 us: 1.35x faster                                                 |
| mako                     | 16.3 ms                                                | 12.1 ms: 1.35x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 756 ms: 1.35x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.2 ms: 1.35x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                |
| nqueens                  | 106 ms                                                 | 79.2 ms: 1.34x faster                                                 |
| sympy_str                | 346 ms                                                 | 260 ms: 1.33x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                 |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                  |
| sympy_expand             | 566 ms                                                 | 443 ms: 1.28x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 51.2 ns: 1.17x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 852 us: 1.16x faster                                                  |
| regex_dna                | 227 ms                                                 | 198 ms: 1.15x faster                                                  |
| async_generators         | 444 ms                                                 | 392 ms: 1.13x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 88.0 ms: 1.13x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| unpickle_list            | 5.20 us                                                | 4.71 us: 1.10x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                 |
| meteor_contest           | 120 ms                                                 | 113 ms: 1.06x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                 |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                 |
| unpickle                 | 14.4 us                                                | 14.1 us: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.30 us: 1.04x slower                                                 |
| pidigits                 | 191 ms                                                 | 203 ms: 1.06x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.7 us: 1.17x slower                                                 |
| pickle                   | 10.7 us                                                | 13.3 us: 1.25x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.97 ms: 1.37x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                 |
| dask                     | 441 ms                                                 | 886 ms: 2.01x slower                                                  |
| logging_silent           | 190 ns                                                 | 503 ns: 2.65x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 92.7 ms: 3.86x slower                                                 |
| coverage                 | 79.4 ms                                                | 399 ms: 5.02x slower                                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 138.17x slower                                                |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (23) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.32x