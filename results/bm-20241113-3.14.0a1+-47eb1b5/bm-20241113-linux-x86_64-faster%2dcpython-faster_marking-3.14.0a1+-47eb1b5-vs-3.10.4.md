# Results vs. 3.10.4

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 47eb1b5
- commit date: 2024-11-13
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                       |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                     |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 596 ms: 2.97x faster                                                       |
| async_tree_none         | 728 ms                                                 | 278 ms: 2.62x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 345 ms: 2.52x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 504 ms: 2.02x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 98.4 ms: 1.56x faster                                                      |
| float          | 117 ms                                                 | 83.9 ms: 1.40x faster                                                      |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                      |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.14x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 61.2 ms: 1.29x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                      |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.2 ms: 1.14x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 172 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 120 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.25x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.4 ms: 1.17x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 6.79 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                      |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 51.6 ms: 1.28x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                                       |
| generators               | 80.1 ms                                                | 26.7 ms: 2.99x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 596 ms: 2.97x faster                                                       |
| async_tree_none          | 728 ms                                                 | 278 ms: 2.62x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 345 ms: 2.52x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.40 ms: 2.33x faster                                                      |
| pylint                   | 551 ms                                                 | 262 ms: 2.10x faster                                                       |
| gc_traversal             | 3.62 ms                                                | 1.74 ms: 2.08x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 504 ms: 2.02x faster                                                       |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.92x faster                                                      |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                                      |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                       |
| richards_super           | 94.7 ms                                                | 52.2 ms: 1.82x faster                                                      |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                       |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                      |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                       |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.0 ms: 1.71x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.17 ms: 1.69x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                      |
| nbody                    | 154 ms                                                 | 98.4 ms: 1.56x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                     |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                      |
| pyflate                  | 716 ms                                                 | 479 ms: 1.50x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                      |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                                       |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                       |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                     |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                      |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                      |
| float                    | 117 ms                                                 | 83.9 ms: 1.40x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                      |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                       |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.35x faster                                                       |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                       |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.89 ms: 1.32x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.32x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 64.4 ms: 1.31x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                      |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 61.2 ms: 1.29x faster                                                      |
| nqueens                  | 106 ms                                                 | 82.1 ms: 1.29x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 51.6 ms: 1.28x faster                                                      |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 54.4 ms: 1.27x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                     |
| scimark_fft              | 466 ms                                                 | 370 ms: 1.26x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                      |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                       |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.4 ms: 1.17x faster                                                      |
| json                     | 5.69 ms                                                | 4.85 ms: 1.17x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 851 us: 1.16x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 87.2 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                       |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                       |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.64 ms: 1.01x slower                                                      |
| xml_etree_parse          | 168 ms                                                 | 172 ms: 1.02x slower                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 120 ms: 1.04x slower                                                       |
| coverage                 | 79.4 ms                                                | 83.9 ms: 1.06x slower                                                      |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 6.79 ms: 1.14x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 84.3 ms: 3.51x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241113-3.14.0a1+-47eb1b5/bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.440x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.24x