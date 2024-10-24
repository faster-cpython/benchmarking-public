# Results vs. 3.10.4

- fork: faster-cpython
- ref: load_int
- machine: linux-x86_64
- commit hash: 1b5b50f
- commit date: 2024-10-24
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                 |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                               |
| html5lib       | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                |
| tornado_http   | 136 ms                                                 | 90.1 ms: 1.51x faster                                                |
| Geometric mean | (ref)                                                  | 1.38x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 838 ms: 2.11x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 413 ms: 2.11x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 96.0 ms: 1.60x faster                                                |
| float          | 117 ms                                                 | 79.3 ms: 1.48x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.16x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.07x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.7 ms: 1.24x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                |
| django_template | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                                 |
| generators               | 80.1 ms                                                | 28.3 ms: 2.83x faster                                                |
| deltablue                | 7.91 ms                                                | 3.30 ms: 2.40x faster                                                |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 838 ms: 2.11x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 413 ms: 2.11x faster                                                 |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                 |
| chaos                    | 115 ms                                                 | 60.8 ms: 1.90x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                 |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                 |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                 |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                 |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                 |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 73.6 ms: 1.74x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                                |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                |
| richards                 | 79.3 ms                                                | 46.9 ms: 1.69x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                                 |
| nbody                    | 154 ms                                                 | 96.0 ms: 1.60x faster                                                |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                 |
| tornado_http             | 136 ms                                                 | 90.1 ms: 1.51x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                               |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.48x faster                                                |
| float                    | 117 ms                                                 | 79.3 ms: 1.48x faster                                                |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                 |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                |
| html5lib                 | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                 |
| django_template          | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                 |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                                |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                                |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                 |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                 |
| python_startup           | 14.6 ms                                                | 11.7 ms: 1.24x faster                                                |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                               |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                |
| json                     | 5.69 ms                                                | 4.83 ms: 1.18x faster                                                |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.16x faster                                                |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                               |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                 |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                 |
| coverage                 | 79.4 ms                                                | 83.6 ms: 1.05x slower                                                |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.70 ms: 1.30x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 77.8 ms: 3.24x slower                                                |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-1b5b50f/bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x