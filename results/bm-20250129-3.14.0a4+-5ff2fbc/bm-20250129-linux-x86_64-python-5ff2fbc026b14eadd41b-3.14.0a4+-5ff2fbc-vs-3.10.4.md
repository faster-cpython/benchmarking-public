# Results vs. 3.10.4

- fork: python
- ref: 5ff2fbc026b14eadd41b
- machine: linux-x86_64
- commit hash: 5ff2fbc
- commit date: 2025-01-29
- overall geometric mean: 1.450x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                   |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 324 ms: 2.69x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.3 ms: 1.63x faster                                                  |
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                  |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 96.4 ms: 1.20x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 48.2 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 156 us: 3.48x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                   |
| generators               | 80.1 ms                                                | 28.5 ms: 2.81x faster                                                  |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 324 ms: 2.69x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                   |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                   |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                   |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                  |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                   |
| richards_super           | 94.7 ms                                                | 50.8 ms: 1.87x faster                                                  |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                   |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                                  |
| richards                 | 79.3 ms                                                | 44.9 ms: 1.76x faster                                                  |
| spectral_norm            | 170 ms                                                 | 96.6 ms: 1.76x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                  |
| logging_silent           | 190 ns                                                 | 110 ns: 1.73x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 69.3 ms: 1.71x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                  |
| nbody                    | 154 ms                                                 | 94.3 ms: 1.63x faster                                                  |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                 |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                  |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.44 us: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                   |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                   |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.44x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.43x faster                                                  |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                  |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 102 ms: 1.40x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.68 ms: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 48.2 ms: 1.37x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                  |
| scimark_fft              | 466 ms                                                 | 344 ms: 1.35x faster                                                   |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 51.5 ms: 1.34x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 63.7 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                  |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.31x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                  |
| sympy_str                | 346 ms                                                 | 264 ms: 1.31x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| sympy_expand             | 566 ms                                                 | 447 ms: 1.27x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 96.4 ms: 1.20x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                  |
| async_generators         | 444 ms                                                 | 380 ms: 1.17x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.46 sec: 1.16x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                  |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                  |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                                  |
| coverage                 | 79.4 ms                                                | 92.0 ms: 1.16x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-5ff2fbc/bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.450x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x