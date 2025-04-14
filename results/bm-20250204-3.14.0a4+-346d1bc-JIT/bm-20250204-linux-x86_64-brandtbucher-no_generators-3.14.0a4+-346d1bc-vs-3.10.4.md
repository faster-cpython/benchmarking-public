# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_generators
- machine: linux-x86_64
- commit hash: 346d1bc
- commit date: 2025-02-04
- overall geometric mean: 1.445x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 622 ms: 2.85x faster                                                  |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 327 ms: 2.66x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.06x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.4 ms: 1.74x faster                                                 |
| nbody          | 154 ms                                                 | 90.1 ms: 1.70x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.45x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 2.97 ms: 1.22x faster                                                 |
| regex_dna      | 227 ms                                                 | 194 ms: 1.17x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.82 sec: 1.73x faster                                                |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.65x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 94.6 ms: 1.22x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                 |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 54.4 ms: 1.21x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 622 ms: 2.85x faster                                                  |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                                 |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 327 ms: 2.66x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.51 ms: 2.25x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.06x faster                                                  |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                  |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.93x faster                                                 |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.92x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.92x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                 |
| go                       | 240 ms                                                 | 127 ms: 1.89x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                 |
| richards                 | 79.3 ms                                                | 43.3 ms: 1.83x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 70.1 ms: 1.82x faster                                                 |
| spectral_norm            | 170 ms                                                 | 93.4 ms: 1.82x faster                                                 |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                  |
| raytrace                 | 507 ms                                                 | 289 ms: 1.76x faster                                                  |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                  |
| float                    | 117 ms                                                 | 67.4 ms: 1.74x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.82 sec: 1.73x faster                                                |
| nbody                    | 154 ms                                                 | 90.1 ms: 1.70x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.65x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                 |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                 |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                 |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                  |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                  |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.42 ms: 1.40x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.64 ms: 1.40x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                                  |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                  |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                                 |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 66.8 ms: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| regex_effbot             | 3.63 ms                                                | 2.97 ms: 1.22x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 94.6 ms: 1.22x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 54.4 ms: 1.21x faster                                                 |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                  |
| nqueens                  | 106 ms                                                 | 89.8 ms: 1.18x faster                                                 |
| regex_dna                | 227 ms                                                 | 194 ms: 1.17x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                  |
| async_generators         | 444 ms                                                 | 408 ms: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                                 |
| coverage                 | 79.4 ms                                                | 90.7 ms: 1.14x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.86 ms: 1.34x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250204-3.14.0a4+-346d1bc-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.445x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x