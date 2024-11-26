# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-aarch64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.189x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 336 ms: 1.13x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.62 sec: 1.03x slower                                                 |
| html5lib       | 86.5 ms                                                               | 72.9 ms: 1.19x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 473 ms: 2.01x faster                                                   |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.91x faster                                                 |
| async_tree_memoization  | 1.13 sec                                                              | 625 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 788 ms: 1.61x faster                                                   |
| Geometric mean          | (ref)                                                                 | 1.83x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 96.2 ms: 1.40x faster                                                  |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 162 ms: 1.09x faster                                                   |
| regex_dna      | 257 ms                                                                | 265 ms: 1.03x slower                                                   |
| regex_v8       | 32.2 ms                                                               | 33.3 ms: 1.04x slower                                                  |
| regex_effbot   | 4.25 ms                                                               | 5.05 ms: 1.19x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 257 us: 1.42x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                 |
| xml_etree_process    | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                  |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 196 ms: 1.08x faster                                                   |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.93 ms: 1.30x slower                                                  |
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.36x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                  |
| django_template | 53.3 ms                                                               | 50.1 ms: 1.06x faster                                                  |
| genshi_xml      | 69.8 ms                                                               | 83.2 ms: 1.19x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 223 us: 2.97x faster                                                   |
| deltablue                | 8.94 ms                                                               | 4.31 ms: 2.07x faster                                                  |
| async_tree_none          | 950 ms                                                                | 473 ms: 2.01x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.91x faster                                                 |
| async_tree_memoization   | 1.13 sec                                                              | 625 ms: 1.81x faster                                                   |
| richards_super           | 107 ms                                                                | 62.6 ms: 1.71x faster                                                  |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 788 ms: 1.61x faster                                                   |
| richards                 | 91.7 ms                                                               | 56.8 ms: 1.61x faster                                                  |
| raytrace                 | 573 ms                                                                | 364 ms: 1.57x faster                                                   |
| scimark_sor              | 246 ms                                                                | 163 ms: 1.51x faster                                                   |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.51x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.50x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 41.4 us: 1.49x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 90.5 ms: 1.48x faster                                                  |
| chaos                    | 121 ms                                                                | 84.6 ms: 1.43x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                  |
| sqlglot_transpile        | 2.84 ms                                                               | 2.00 ms: 1.42x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 257 us: 1.42x faster                                                   |
| generators               | 68.1 ms                                                               | 48.4 ms: 1.41x faster                                                  |
| float                    | 135 ms                                                                | 96.2 ms: 1.40x faster                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 92.4 ms: 1.38x faster                                                  |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                                   |
| go                       | 264 ms                                                                | 193 ms: 1.37x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                                   |
| comprehensions           | 33.1 us                                                               | 25.0 us: 1.33x faster                                                  |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                  |
| deepcopy                 | 511 us                                                                | 400 us: 1.28x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 155 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                 |
| logging_format           | 10.6 us                                                               | 8.46 us: 1.25x faster                                                  |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.25x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.84 us: 1.25x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                  |
| spectral_norm            | 186 ms                                                                | 154 ms: 1.21x faster                                                   |
| pyflate                  | 795 ms                                                                | 661 ms: 1.20x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 72.9 ms: 1.19x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                                  |
| pylint                   | 485 ms                                                                | 419 ms: 1.16x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.15x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 4.02 us: 1.14x faster                                                  |
| 2to3                     | 381 ms                                                                | 336 ms: 1.13x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.51 sec: 1.12x faster                                                 |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                   |
| sqlalchemy_imperative    | 20.5 ms                                                               | 18.5 ms: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                   |
| regex_compile            | 177 ms                                                                | 162 ms: 1.09x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.1 ms: 1.09x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 196 ms: 1.08x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 24.8 ms: 1.07x faster                                                  |
| django_template          | 53.3 ms                                                               | 50.1 ms: 1.06x faster                                                  |
| sympy_sum                | 184 ms                                                                | 174 ms: 1.06x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.05x faster                                                   |
| fannkuch                 | 546 ms                                                                | 523 ms: 1.04x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 72.4 ms: 1.04x faster                                                  |
| mdp                      | 3.70 sec                                                              | 3.60 sec: 1.03x faster                                                 |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.62 sec: 1.03x slower                                                 |
| regex_dna                | 257 ms                                                                | 265 ms: 1.03x slower                                                   |
| regex_v8                 | 32.2 ms                                                               | 33.3 ms: 1.04x slower                                                  |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                  |
| nqueens                  | 117 ms                                                                | 126 ms: 1.07x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.54 sec: 1.08x slower                                                 |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                                 |
| dulwich_log              | 73.5 ms                                                               | 80.0 ms: 1.09x slower                                                  |
| sympy_expand             | 543 ms                                                                | 592 ms: 1.09x slower                                                   |
| async_generators         | 452 ms                                                                | 531 ms: 1.17x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                  |
| coverage                 | 83.6 ms                                                               | 99.0 ms: 1.19x slower                                                  |
| regex_effbot             | 4.25 ms                                                               | 5.05 ms: 1.19x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 83.2 ms: 1.19x slower                                                  |
| python_startup_no_site   | 6.89 ms                                                               | 8.93 ms: 1.30x slower                                                  |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                  |
| gc_traversal             | 4.15 ms                                                               | 6.43 ms: 1.55x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 2.11 sec: 145.37x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                           |

Benchmark hidden because not significant (8): scimark_sparse_mat_mult, genshi_text, sqlite_synth, json, xml_etree_iterparse, meteor_contest, pidigits, sympy_str
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.189x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.32x