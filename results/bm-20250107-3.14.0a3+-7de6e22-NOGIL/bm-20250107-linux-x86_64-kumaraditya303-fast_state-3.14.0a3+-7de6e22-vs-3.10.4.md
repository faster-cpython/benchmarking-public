# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 345 ms: 1.01x faster                                                 |
| docutils       | 3.30 sec                                               | 2.99 sec: 1.10x faster                                               |
| html5lib       | 88.9 ms                                                | 85.7 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 726 ms: 2.44x faster                                                 |
| async_tree_none         | 728 ms                                                 | 339 ms: 2.15x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 430 ms: 2.02x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 580 ms: 1.75x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 136 ms: 1.13x faster                                                 |
| float          | 117 ms                                                 | 105 ms: 1.11x faster                                                 |
| pidigits       | 191 ms                                                 | 181 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 162 ms: 1.16x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.55 sec: 1.23x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 95.7 ms: 1.21x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 72.3 ms: 1.09x faster                                                |
| json_dumps           | 14.2 ms                                                | 13.0 ms: 1.09x faster                                                |
| unpickle_pure_python | 331 us                                                 | 314 us: 1.05x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 96.2 ms: 1.03x faster                                                |
| json_loads           | 31.2 us                                                | 30.3 us: 1.03x faster                                                |
| pickle_pure_python   | 484 us                                                 | 482 us: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                |
| python_startup_no_site | 5.93 ms                                                | 9.59 ms: 1.62x slower                                                |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 66.0 ms                                                | 63.0 ms: 1.05x faster                                                |
| genshi_text     | 31.8 ms                                                | 30.4 ms: 1.05x faster                                                |
| django_template | 48.2 ms                                                | 46.5 ms: 1.04x faster                                                |
| mako            | 16.3 ms                                                | 18.2 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 206 us: 2.64x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 726 ms: 2.44x faster                                                 |
| generators               | 80.1 ms                                                | 35.9 ms: 2.23x faster                                                |
| async_tree_none          | 728 ms                                                 | 339 ms: 2.15x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 430 ms: 2.02x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 580 ms: 1.75x faster                                                 |
| pylint                   | 551 ms                                                 | 341 ms: 1.62x faster                                                 |
| deepcopy                 | 479 us                                                 | 319 us: 1.50x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 40.3 us: 1.45x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 92.3 ms: 1.38x faster                                                |
| richards_super           | 94.7 ms                                                | 70.3 ms: 1.35x faster                                                |
| spectral_norm            | 170 ms                                                 | 127 ms: 1.34x faster                                                 |
| coroutines               | 35.1 ms                                                | 26.8 ms: 1.31x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 3.32 us: 1.26x faster                                                |
| richards                 | 79.3 ms                                                | 63.1 ms: 1.26x faster                                                |
| chaos                    | 115 ms                                                 | 92.7 ms: 1.25x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.55 sec: 1.23x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 95.7 ms: 1.21x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                |
| regex_compile            | 188 ms                                                 | 162 ms: 1.16x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.37 sec: 1.15x faster                                               |
| scimark_lu               | 176 ms                                                 | 154 ms: 1.14x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                 |
| comprehensions           | 28.8 us                                                | 25.4 us: 1.13x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 105 ms: 1.13x faster                                                 |
| nbody                    | 154 ms                                                 | 136 ms: 1.13x faster                                                 |
| deltablue                | 7.91 ms                                                | 7.05 ms: 1.12x faster                                                |
| dulwich_log              | 84.3 ms                                                | 75.5 ms: 1.12x faster                                                |
| scimark_fft              | 466 ms                                                 | 417 ms: 1.12x faster                                                 |
| float                    | 117 ms                                                 | 105 ms: 1.11x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 129 ms: 1.10x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.99 sec: 1.10x faster                                               |
| pyflate                  | 716 ms                                                 | 651 ms: 1.10x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                |
| go                       | 240 ms                                                 | 218 ms: 1.10x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 72.3 ms: 1.09x faster                                                |
| hexiom                   | 10.4 ms                                                | 9.50 ms: 1.09x faster                                                |
| raytrace                 | 507 ms                                                 | 465 ms: 1.09x faster                                                 |
| json_dumps               | 14.2 ms                                                | 13.0 ms: 1.09x faster                                                |
| logging_silent           | 190 ns                                                 | 176 ns: 1.08x faster                                                 |
| sympy_sum                | 196 ms                                                 | 183 ms: 1.07x faster                                                 |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 64.7 ms: 1.07x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 956 ms: 1.07x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.98 sec: 1.06x faster                                               |
| thrift                   | 1.07 ms                                                | 1.01 ms: 1.06x faster                                                |
| nqueens                  | 106 ms                                                 | 99.8 ms: 1.06x faster                                                |
| pidigits                 | 191 ms                                                 | 181 ms: 1.05x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 24.5 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.14 ms: 1.05x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 314 us: 1.05x faster                                                 |
| logging_simple           | 8.30 us                                                | 7.92 us: 1.05x faster                                                |
| genshi_xml               | 66.0 ms                                                | 63.0 ms: 1.05x faster                                                |
| genshi_text              | 31.8 ms                                                | 30.4 ms: 1.05x faster                                                |
| sympy_str                | 346 ms                                                 | 333 ms: 1.04x faster                                                 |
| html5lib                 | 88.9 ms                                                | 85.7 ms: 1.04x faster                                                |
| django_template          | 48.2 ms                                                | 46.5 ms: 1.04x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 96.2 ms: 1.03x faster                                                |
| logging_format           | 9.09 us                                                | 8.81 us: 1.03x faster                                                |
| json_loads               | 31.2 us                                                | 30.3 us: 1.03x faster                                                |
| sympy_expand             | 566 ms                                                 | 555 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| fannkuch                 | 532 ms                                                 | 526 ms: 1.01x faster                                                 |
| 2to3                     | 348 ms                                                 | 345 ms: 1.01x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 2.55 ms: 1.01x faster                                                |
| pickle_pure_python       | 484 us                                                 | 482 us: 1.00x faster                                                 |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                 |
| sqlglot_parse            | 2.17 ms                                                | 2.21 ms: 1.02x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 180 ms: 1.05x slower                                                 |
| python_startup           | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                |
| meteor_contest           | 120 ms                                                 | 131 ms: 1.10x slower                                                 |
| mako                     | 16.3 ms                                                | 18.2 ms: 1.12x slower                                                |
| async_generators         | 444 ms                                                 | 501 ms: 1.13x slower                                                 |
| telco                    | 7.27 ms                                                | 9.21 ms: 1.27x slower                                                |
| coverage                 | 79.4 ms                                                | 103 ms: 1.29x slower                                                 |
| mypy2                    | 894 ms                                                 | 1.20 sec: 1.35x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.33 ms: 1.44x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 9.59 ms: 1.62x slower                                                |
| bench_thread_pool        | 986 us                                                 | 3.56 ms: 3.61x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 95.0 ms: 3.96x slower                                                |
| Geometric mean           | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (4): regex_effbot, mdp, sqlalchemy_imperative, scimark_sor
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.50x