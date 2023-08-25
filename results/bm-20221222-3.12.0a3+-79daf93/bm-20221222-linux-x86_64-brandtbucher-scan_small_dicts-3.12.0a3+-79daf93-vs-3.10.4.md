
# Results vs. 3.10.4

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 79daf93
- commit date: 2022-12-22
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.54 ms: 1.39x faster                                                    |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                   |
| html5lib       | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.2 ms: 1.51x faster                                                    |
| nbody          | 142 ms                                                 | 94.7 ms: 1.50x faster                                                    |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                    |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 278 us: 1.64x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 54.0 ms: 1.39x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 78.1 ms: 1.21x faster                                                    |
| json_loads           | 28.8 us                                                | 24.1 us: 1.19x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.11 us: 1.11x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                     |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                    |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                                    |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.56 ms: 1.65x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.12 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.51 ms: 1.55x faster                                                    |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                    |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 47.4 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                    |
| logging_silent          | 175 ns                                                 | 91.2 ns: 1.92x faster                                                    |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                     |
| richards                | 74.9 ms                                                | 41.9 ms: 1.79x faster                                                    |
| go                      | 229 ms                                                 | 132 ms: 1.74x faster                                                     |
| pyflate                 | 673 ms                                                 | 397 ms: 1.70x faster                                                     |
| raytrace                | 464 ms                                                 | 279 ms: 1.66x faster                                                     |
| python_startup          | 14.2 ms                                                | 8.56 ms: 1.65x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 65.9 ms: 1.64x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 278 us: 1.64x faster                                                     |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.60x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 32.9 us: 1.59x faster                                                    |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.57x faster                                                    |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.56x faster                                                    |
| mako                    | 14.8 ms                                                | 9.51 ms: 1.55x faster                                                    |
| unpack_sequence         | 64.7 ns                                                | 42.1 ns: 1.54x faster                                                    |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                     |
| float                   | 111 ms                                                 | 73.2 ms: 1.51x faster                                                    |
| nbody                   | 142 ms                                                 | 94.7 ms: 1.50x faster                                                    |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                    |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                   |
| html5lib                | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                    |
| pprint_safe_repr        | 955 ms                                                 | 666 ms: 1.43x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.63 us: 1.43x faster                                                    |
| logging_format          | 8.91 us                                                | 6.22 us: 1.43x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                    |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                    |
| xml_etree_process       | 74.9 ms                                                | 54.0 ms: 1.39x faster                                                    |
| chameleon               | 9.06 ms                                                | 6.54 ms: 1.39x faster                                                    |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                     |
| deepcopy                | 442 us                                                 | 322 us: 1.37x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                                   |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                     |
| scimark_fft             | 424 ms                                                 | 316 ms: 1.34x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 47.4 ms: 1.34x faster                                                    |
| async_tree_none         | 717 ms                                                 | 537 ms: 1.33x faster                                                     |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.34 sec: 1.33x faster                                                   |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.89 us: 1.32x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 651 ms: 1.31x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                    |
| coroutines              | 31.8 ms                                                | 24.8 ms: 1.29x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                                    |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.27x faster                                                    |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 768 ms: 1.24x faster                                                     |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 778 us: 1.22x faster                                                     |
| dulwich_log             | 75.9 ms                                                | 62.5 ms: 1.21x faster                                                    |
| xml_etree_generate      | 94.2 ms                                                | 78.1 ms: 1.21x faster                                                    |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                     |
| json_loads              | 28.8 us                                                | 24.1 us: 1.19x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                                    |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                    |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                    |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                                     |
| pickle_list             | 4.56 us                                                | 4.11 us: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| djangocms               | 35.9 us                                                | 32.8 us: 1.09x faster                                                    |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                     |
| json                    | 5.42 ms                                                | 5.03 ms: 1.08x faster                                                    |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                    |
| meteor_contest          | 115 ms                                                 | 108 ms: 1.07x faster                                                     |
| telco                   | 6.54 ms                                                | 6.24 ms: 1.05x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.71 sec: 1.04x faster                                                   |
| generators              | 76.8 ms                                                | 74.8 ms: 1.03x faster                                                    |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                    |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                                    |
| python_startup_no_site  | 5.82 ms                                                | 6.12 ms: 1.05x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                    |
| pickle_dict             | 27.3 us                                                | 31.2 us: 1.14x slower                                                    |
| coverage                | 72.8 ms                                                | 97.5 ms: 1.34x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221222-3.12.0a3+-79daf93/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
