
# Results vs. 3.10.4

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: ba16621
- commit date: 2022-12-17
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                    |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                   |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.0 ms: 1.53x faster                                                    |
| nbody          | 142 ms                                                 | 94.1 ms: 1.50x faster                                                    |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                    |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 53.2 ms: 1.41x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 76.2 ms: 1.24x faster                                                    |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.10 us: 1.11x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                                     |
| unpickle             | 14.1 us                                                | 13.0 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.05x faster                                                     |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                    |
| unpickle_list        | 4.82 us                                                | 5.09 us: 1.06x slower                                                    |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.51 ms: 1.66x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.09 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.42 ms: 1.57x faster                                                    |
| genshi_text     | 30.3 ms                                                | 20.3 ms: 1.49x faster                                                    |
| django_template | 45.9 ms                                                | 32.2 ms: 1.43x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 46.9 ms: 1.35x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                    |
| logging_silent          | 175 ns                                                 | 91.9 ns: 1.90x faster                                                    |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                     |
| richards                | 74.9 ms                                                | 42.0 ms: 1.79x faster                                                    |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                     |
| python_startup          | 14.2 ms                                                | 8.51 ms: 1.66x faster                                                    |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                     |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                                     |
| scimark_monte_carlo     | 108 ms                                                 | 66.0 ms: 1.64x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                                     |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                    |
| chaos                   | 106 ms                                                 | 67.3 ms: 1.58x faster                                                    |
| spectral_norm           | 150 ms                                                 | 95.1 ms: 1.58x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 33.2 us: 1.58x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 75.5 ms: 1.57x faster                                                    |
| mako                    | 14.8 ms                                                | 9.42 ms: 1.57x faster                                                    |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.56x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 42.1 ns: 1.54x faster                                                    |
| float                   | 111 ms                                                 | 72.0 ms: 1.53x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                     |
| nbody                   | 142 ms                                                 | 94.1 ms: 1.50x faster                                                    |
| genshi_text             | 30.3 ms                                                | 20.3 ms: 1.49x faster                                                    |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                    |
| chameleon               | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                    |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| django_template         | 45.9 ms                                                | 32.2 ms: 1.43x faster                                                    |
| pprint_safe_repr        | 955 ms                                                 | 669 ms: 1.43x faster                                                     |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                                    |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                                    |
| xml_etree_process       | 74.9 ms                                                | 53.2 ms: 1.41x faster                                                    |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 754 us: 1.37x faster                                                     |
| deepcopy                | 442 us                                                 | 323 us: 1.37x faster                                                     |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.37x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                    |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 629 ms: 1.36x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 46.9 ms: 1.35x faster                                                    |
| async_tree_none         | 717 ms                                                 | 533 ms: 1.34x faster                                                     |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 50.3 ms: 1.30x faster                                                    |
| nqueens                 | 100 ms                                                 | 77.4 ms: 1.29x faster                                                    |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                     |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                   |
| coroutines              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed | 951 ms                                                 | 758 ms: 1.25x faster                                                     |
| xml_etree_generate      | 94.2 ms                                                | 76.2 ms: 1.24x faster                                                    |
| async_generators        | 425 ms                                                 | 348 ms: 1.22x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 777 us: 1.22x faster                                                     |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                                    |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                    |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                    |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.15x faster                                                    |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.14x faster                                                    |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                                     |
| json                    | 5.42 ms                                                | 4.81 ms: 1.12x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.10 us: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                   |
| djangocms               | 35.9 us                                                | 32.7 us: 1.10x faster                                                    |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                     |
| unpickle                | 14.1 us                                                | 13.0 us: 1.08x faster                                                    |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.05x faster                                                     |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                    |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                                    |
| generators              | 76.8 ms                                                | 77.0 ms: 1.00x slower                                                    |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                     |
| python_startup_no_site  | 5.82 ms                                                | 6.09 ms: 1.05x slower                                                    |
| unpickle_list           | 4.82 us                                                | 5.09 us: 1.06x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.50 ms: 1.09x slower                                                    |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.14x slower                                                    |
| coverage                | 72.8 ms                                                | 101 ms: 1.38x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221217-3.12.0a3+-ba16621/bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
