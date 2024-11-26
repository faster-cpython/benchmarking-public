# Results vs. 3.10.4

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: fb5fdad
- commit date: 2024-11-10
- overall geometric mean: 1.441x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                       |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                     |
| html5lib       | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 627 ms: 2.82x faster                                                       |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 337 ms: 2.58x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 96.3 ms: 1.59x faster                                                      |
| float          | 117 ms                                                 | 78.8 ms: 1.49x faster                                                      |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                      |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 330 us: 1.47x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                      |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.16x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 99.9 ms: 1.16x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 6.83 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                      |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                      |
| django_template | 48.2 ms                                                | 35.0 ms: 1.38x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                       |
| generators               | 80.1 ms                                                | 27.4 ms: 2.93x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 627 ms: 2.82x faster                                                       |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 337 ms: 2.58x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                      |
| pylint                   | 551 ms                                                 | 263 ms: 2.10x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                       |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                                       |
| gc_traversal             | 3.62 ms                                                | 1.89 ms: 1.92x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                      |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                      |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                       |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                       |
| richards_super           | 94.7 ms                                                | 53.0 ms: 1.79x faster                                                      |
| logging_silent           | 190 ns                                                 | 110 ns: 1.72x faster                                                       |
| richards                 | 79.3 ms                                                | 46.6 ms: 1.70x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.70x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.9 ms: 1.69x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                      |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.40 ms: 1.62x faster                                                      |
| nbody                    | 154 ms                                                 | 96.3 ms: 1.59x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                      |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                       |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                      |
| float                    | 117 ms                                                 | 78.8 ms: 1.49x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                                      |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 330 us: 1.47x faster                                                       |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.46x faster                                                       |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                       |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                      |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                      |
| thrift                   | 1.07 ms                                                | 774 us: 1.38x faster                                                       |
| html5lib                 | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                       |
| django_template          | 48.2 ms                                                | 35.0 ms: 1.38x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.35x faster                                                       |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                       |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.99 ms: 1.30x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 65.3 ms: 1.29x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                      |
| scimark_fft              | 466 ms                                                 | 364 ms: 1.28x faster                                                       |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                                      |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                      |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                      |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.16x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 99.9 ms: 1.16x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 856 us: 1.15x faster                                                       |
| json                     | 5.69 ms                                                | 4.95 ms: 1.15x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                      |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                       |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                       |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.08x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 6.83 ms: 1.15x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241110-3.14.0a1+-fb5fdad/bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.441x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x