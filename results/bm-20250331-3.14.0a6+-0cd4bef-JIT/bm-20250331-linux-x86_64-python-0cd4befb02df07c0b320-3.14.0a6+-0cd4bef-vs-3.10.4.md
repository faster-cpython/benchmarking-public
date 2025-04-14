# Results vs. 3.10.4

- fork: python
- ref: 0cd4befb02df07c0b320
- machine: linux-x86_64
- commit hash: 0cd4bef
- commit date: 2025-03-31
- overall geometric mean: 1.462x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                   |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.89x faster                                                   |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 63.9 ms: 1.83x faster                                                  |
| nbody          | 154 ms                                                 | 85.6 ms: 1.79x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.50x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.37 ms: 1.08x faster                                                  |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                  |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                  |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                  |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.89x faster                                                   |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                  |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                                  |
| richards_super           | 94.7 ms                                                | 40.6 ms: 2.33x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.28x faster                                                 |
| richards                 | 79.3 ms                                                | 35.5 ms: 2.24x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                  |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                   |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                  |
| logging_silent           | 190 ns                                                 | 97.8 ns: 1.94x faster                                                  |
| go                       | 240 ms                                                 | 126 ms: 1.90x faster                                                   |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                   |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                   |
| float                    | 117 ms                                                 | 63.9 ms: 1.83x faster                                                  |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                   |
| spectral_norm            | 170 ms                                                 | 94.0 ms: 1.81x faster                                                  |
| nbody                    | 154 ms                                                 | 85.6 ms: 1.79x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.72x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                 |
| pyflate                  | 716 ms                                                 | 429 ms: 1.67x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                   |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.55x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.81 ms: 1.53x faster                                                  |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                   |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                   |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                  |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 60.5 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                 |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 773 ms: 1.32x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                  |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                   |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                   |
| nqueens                  | 106 ms                                                 | 83.1 ms: 1.27x faster                                                  |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| sympy_expand             | 566 ms                                                 | 475 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 885 us: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.37 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                  |
| async_generators         | 444 ms                                                 | 416 ms: 1.07x faster                                                   |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                  |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.08x slower                                                  |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.06 ms: 1.40x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 83.1 ms: 3.46x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.462x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.30x