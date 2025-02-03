# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.262x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 305 ms: 1.14x faster                                                   |
| docutils       | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                 |
| html5lib       | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                                   |
| async_tree_none         | 728 ms                                                 | 286 ms: 2.55x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 364 ms: 2.39x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 523 ms: 1.94x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.43x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 78.7 ms: 1.49x faster                                                  |
| nbody          | 154 ms                                                 | 139 ms: 1.10x faster                                                   |
| pidigits       | 191 ms                                                 | 182 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 147 ms: 1.28x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                  |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.38 sec: 1.32x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 368 us: 1.32x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 254 us: 1.30x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 94.6 ms: 1.22x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 67.7 ms: 1.17x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                   |
| json_dumps           | 14.2 ms                                                | 12.7 ms: 1.12x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 95.0 ms: 1.05x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| json_loads           | 31.2 us                                                | 33.2 us: 1.06x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.74 us: 1.10x slower                                                  |
| unpickle             | 14.4 us                                                | 16.1 us: 1.12x slower                                                  |
| pickle               | 10.7 us                                                | 12.4 us: 1.16x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.0 ms: 1.03x slower                                                  |
| python_startup_no_site | 5.93 ms                                                | 9.36 ms: 1.58x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 40.1 ms: 1.20x faster                                                  |
| genshi_text     | 31.8 ms                                                | 28.2 ms: 1.13x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                  |
| mako            | 16.3 ms                                                | 16.3 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                                   |
| typing_runtime_protocols | 544 us                                                 | 202 us: 2.69x faster                                                   |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                  |
| async_tree_none          | 728 ms                                                 | 286 ms: 2.55x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 364 ms: 2.39x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 523 ms: 1.94x faster                                                   |
| pylint                   | 551 ms                                                 | 308 ms: 1.79x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 539 ms: 1.71x faster                                                   |
| logging_silent           | 190 ns                                                 | 111 ns: 1.70x faster                                                   |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                   |
| deltablue                | 7.91 ms                                                | 4.73 ms: 1.67x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 2.25 ms: 1.61x faster                                                  |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.59x faster                                                   |
| chaos                    | 115 ms                                                 | 74.6 ms: 1.55x faster                                                  |
| deepcopy                 | 479 us                                                 | 310 us: 1.55x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 39.1 us: 1.50x faster                                                  |
| richards_super           | 94.7 ms                                                | 63.3 ms: 1.50x faster                                                  |
| float                    | 117 ms                                                 | 78.7 ms: 1.49x faster                                                  |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                   |
| richards                 | 79.3 ms                                                | 54.4 ms: 1.46x faster                                                  |
| raytrace                 | 507 ms                                                 | 349 ms: 1.45x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 88.7 ms: 1.44x faster                                                  |
| comprehensions           | 28.8 us                                                | 20.0 us: 1.44x faster                                                  |
| coroutines               | 35.1 ms                                                | 24.6 ms: 1.43x faster                                                  |
| pyflate                  | 716 ms                                                 | 510 ms: 1.40x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.57 ms: 1.38x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.90 ms: 1.35x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 87.6 ms: 1.35x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.85 ms: 1.32x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.38 sec: 1.32x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 368 us: 1.32x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                 |
| html5lib                 | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 254 us: 1.30x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 3.25 us: 1.28x faster                                                  |
| regex_compile            | 188 ms                                                 | 147 ms: 1.28x faster                                                   |
| logging_simple           | 8.30 us                                                | 6.60 us: 1.26x faster                                                  |
| scimark_lu               | 176 ms                                                 | 140 ms: 1.25x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.05 sec: 1.25x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                  |
| logging_format           | 9.09 us                                                | 7.38 us: 1.23x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 94.6 ms: 1.22x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.73 sec: 1.21x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 841 ms: 1.21x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 118 ms: 1.21x faster                                                   |
| django_template          | 48.2 ms                                                | 40.1 ms: 1.20x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 67.7 ms: 1.17x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.3 ms: 1.15x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 60.1 ms: 1.15x faster                                                  |
| thrift                   | 1.07 ms                                                | 935 us: 1.15x faster                                                   |
| unpack_sequence          | 60.0 ns                                                | 52.5 ns: 1.14x faster                                                  |
| 2to3                     | 348 ms                                                 | 305 ms: 1.14x faster                                                   |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                   |
| genshi_text              | 31.8 ms                                                | 28.2 ms: 1.13x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                   |
| json_dumps               | 14.2 ms                                                | 12.7 ms: 1.12x faster                                                  |
| scimark_fft              | 466 ms                                                 | 419 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 23.4 ms: 1.10x faster                                                  |
| nbody                    | 154 ms                                                 | 139 ms: 1.10x faster                                                   |
| sympy_str                | 346 ms                                                 | 315 ms: 1.10x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 159 ms: 1.09x faster                                                   |
| sympy_expand             | 566 ms                                                 | 521 ms: 1.09x faster                                                   |
| nqueens                  | 106 ms                                                 | 99.6 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.09 ms: 1.06x faster                                                  |
| pidigits                 | 191 ms                                                 | 182 ms: 1.05x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 95.0 ms: 1.05x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                  |
| fannkuch                 | 532 ms                                                 | 519 ms: 1.02x faster                                                   |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| mako                     | 16.3 ms                                                | 16.3 ms: 1.00x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| python_startup           | 14.6 ms                                                | 15.0 ms: 1.03x slower                                                  |
| json_loads               | 31.2 us                                                | 33.2 us: 1.06x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                  |
| meteor_contest           | 120 ms                                                 | 131 ms: 1.09x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.74 us: 1.10x slower                                                  |
| unpickle                 | 14.4 us                                                | 16.1 us: 1.12x slower                                                  |
| pickle                   | 10.7 us                                                | 12.4 us: 1.16x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.17x slower                                                  |
| telco                    | 7.27 ms                                                | 9.18 ms: 1.26x slower                                                  |
| coverage                 | 79.4 ms                                                | 107 ms: 1.35x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 9.36 ms: 1.58x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 84.8 ms: 3.53x slower                                                  |
| bench_thread_pool        | 986 us                                                 | 3.48 ms: 3.53x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (2): mdp, json
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.262x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.50x