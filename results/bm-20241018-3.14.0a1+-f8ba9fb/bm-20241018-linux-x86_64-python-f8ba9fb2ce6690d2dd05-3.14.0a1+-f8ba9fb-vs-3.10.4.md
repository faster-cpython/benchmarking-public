# Results vs. 3.10.4

- fork: python
- ref: f8ba9fb2ce6690d2dd05
- machine: linux-x86_64
- commit hash: f8ba9fb
- commit date: 2024-10-18
- overall geometric mean: 1.403x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                  |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.09x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 851 ms: 2.08x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 575 ms: 1.77x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.0 ms: 1.65x faster                                                  |
| float          | 117 ms                                                 | 79.9 ms: 1.47x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                  |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| json_loads           | 31.2 us                                                | 26.4 us: 1.18x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                   |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.21 us: 1.03x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.57 us: 1.07x slower                                                  |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                  |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                  |
| mako            | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                                   |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                                  |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.09x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 851 ms: 2.08x faster                                                   |
| go                       | 240 ms                                                 | 120 ms: 1.99x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.91x faster                                                   |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                                  |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 31.1 us: 1.88x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                   |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                                  |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 575 ms: 1.77x faster                                                   |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                   |
| richards                 | 79.3 ms                                                | 45.7 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.8 ms: 1.73x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                  |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                  |
| nbody                    | 154 ms                                                 | 93.0 ms: 1.65x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.37 ms: 1.63x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                   |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                  |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                   |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| float                    | 117 ms                                                 | 79.9 ms: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                  |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                   |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                 |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                   |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                  |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                  |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 44.6 ns: 1.35x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                   |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 63.4 ms: 1.33x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                   |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.29x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                  |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.05 ms: 1.28x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                                   |
| scimark_fft              | 466 ms                                                 | 374 ms: 1.24x faster                                                   |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                 |
| json_loads               | 31.2 us                                                | 26.4 us: 1.18x faster                                                  |
| json                     | 5.69 ms                                                | 4.87 ms: 1.17x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 846 us: 1.17x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.91 us: 1.04x faster                                                  |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                   |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                   |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.21 us: 1.03x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                  |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.57 us: 1.07x slower                                                  |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                  |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                  |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.15x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.73 ms: 1.31x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.67x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 78.0 ms: 3.25x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                           |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241018-3.14.0a1+-f8ba9fb/bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.403x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.26x