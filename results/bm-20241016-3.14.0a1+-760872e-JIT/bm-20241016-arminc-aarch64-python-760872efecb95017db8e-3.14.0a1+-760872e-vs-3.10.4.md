# Results vs. 3.10.4

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-aarch64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.170x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.65 sec: 1.04x slower                                                   |
| html5lib       | 86.5 ms                                                               | 71.5 ms: 1.21x faster                                                    |
| tornado_http   | 178 ms                                                                | 147 ms: 1.21x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 455 ms: 2.09x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 597 ms: 1.90x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 752 ms: 1.69x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.90x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 115 ms: 1.45x faster                                                     |
| float          | 135 ms                                                                | 98.0 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 244 ms: 1.05x faster                                                     |
| regex_compile  | 177 ms                                                                | 169 ms: 1.05x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 31.4 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 268 us: 1.36x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 389 us: 1.36x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.67 us: 1.05x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| json_loads           | 30.9 us                                                               | 31.4 us: 1.02x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.0 us: 1.09x slower                                                    |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                    |
| python_startup         | 11.2 ms                                                               | 14.6 ms: 1.31x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 33.5 ms: 1.05x faster                                                    |
| django_template | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 214 us: 3.09x faster                                                     |
| async_tree_none          | 950 ms                                                                | 455 ms: 2.09x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.52 ms: 1.98x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 597 ms: 1.90x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 752 ms: 1.69x faster                                                     |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                     |
| raytrace                 | 573 ms                                                                | 358 ms: 1.60x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 38.9 us: 1.59x faster                                                    |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                     |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                     |
| richards_super           | 107 ms                                                                | 71.5 ms: 1.50x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 629 ms: 1.50x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 90.2 ms: 1.49x faster                                                    |
| nbody                    | 166 ms                                                                | 115 ms: 1.45x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.44x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                    |
| go                       | 264 ms                                                                | 184 ms: 1.44x faster                                                     |
| richards                 | 91.7 ms                                                               | 64.3 ms: 1.43x faster                                                    |
| chaos                    | 121 ms                                                                | 85.0 ms: 1.42x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 90.1 ms: 1.42x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.70 ms: 1.41x faster                                                    |
| float                    | 135 ms                                                                | 98.0 ms: 1.37x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.36x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 389 us: 1.36x faster                                                     |
| deepcopy                 | 511 us                                                                | 377 us: 1.36x faster                                                     |
| comprehensions           | 33.1 us                                                               | 24.7 us: 1.34x faster                                                    |
| thrift                   | 1.26 ms                                                               | 957 us: 1.32x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.47 us: 1.31x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.18 ms: 1.30x faster                                                    |
| pyflate                  | 795 ms                                                                | 612 ms: 1.30x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.18 us: 1.30x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                    |
| tornado_http             | 178 ms                                                                | 147 ms: 1.21x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 71.5 ms: 1.21x faster                                                    |
| spectral_norm            | 186 ms                                                                | 155 ms: 1.20x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.96 us: 1.16x faster                                                    |
| generators               | 68.1 ms                                                               | 59.0 ms: 1.15x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.48 sec: 1.14x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                     |
| fannkuch                 | 546 ms                                                                | 495 ms: 1.10x faster                                                     |
| scimark_fft              | 500 ms                                                                | 456 ms: 1.10x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.19 ms: 1.06x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.49 sec: 1.06x faster                                                   |
| regex_dna                | 257 ms                                                                | 244 ms: 1.05x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 33.5 ms: 1.05x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.92 us: 1.05x faster                                                    |
| json                     | 5.88 ms                                                               | 5.60 ms: 1.05x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.67 us: 1.05x faster                                                    |
| regex_compile            | 177 ms                                                                | 169 ms: 1.05x faster                                                     |
| django_template          | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.4 ms: 1.02x faster                                                    |
| meteor_contest           | 126 ms                                                                | 125 ms: 1.01x faster                                                     |
| json_loads               | 30.9 us                                                               | 31.4 us: 1.02x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.65 sec: 1.04x slower                                                   |
| nqueens                  | 117 ms                                                                | 122 ms: 1.04x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.20 sec: 1.04x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 78.0 ms: 1.06x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.54 sec: 1.08x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 81.8 ms: 1.09x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.0 us: 1.09x slower                                                    |
| sympy_str                | 329 ms                                                                | 358 ms: 1.09x slower                                                     |
| sympy_expand             | 543 ms                                                                | 592 ms: 1.09x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 29.1 ms: 1.10x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                    |
| async_generators         | 452 ms                                                                | 510 ms: 1.13x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.61 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                    |
| sympy_sum                | 184 ms                                                                | 215 ms: 1.17x slower                                                     |
| coverage                 | 83.6 ms                                                               | 98.9 ms: 1.18x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                    |
| python_startup           | 11.2 ms                                                               | 14.6 ms: 1.31x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.43 ms: 1.55x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.59 sec: 109.33x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (6): sqlglot_normalize, pidigits, 2to3, asyncio_websockets, pickle_list, pylint
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.170x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.37x