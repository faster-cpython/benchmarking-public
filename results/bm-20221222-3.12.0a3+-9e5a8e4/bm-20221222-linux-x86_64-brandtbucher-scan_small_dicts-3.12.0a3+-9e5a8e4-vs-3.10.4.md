
# Results vs. 3.10.4

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 9e5a8e4
- commit date: 2022-12-22
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 255 ms: 1.32x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                    |
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                   |
| html5lib       | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                                    |
| nbody          | 142 ms                                                 | 96.6 ms: 1.47x faster                                                    |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                     |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                    |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 53.2 ms: 1.41x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 76.3 ms: 1.24x faster                                                    |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.09 us: 1.11x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                     |
| unpickle             | 14.1 us                                                | 13.8 us: 1.03x faster                                                    |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                    |
| unpickle_list        | 4.82 us                                                | 5.03 us: 1.04x slower                                                    |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.55 ms: 1.65x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.13 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.37 ms: 1.57x faster                                                    |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                    |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                    |
| logging_silent          | 175 ns                                                 | 90.9 ns: 1.93x faster                                                    |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                                     |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                                     |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                                     |
| python_startup          | 14.2 ms                                                | 8.55 ms: 1.65x faster                                                    |
| richards                | 74.9 ms                                                | 45.6 ms: 1.64x faster                                                    |
| go                      | 229 ms                                                 | 141 ms: 1.63x faster                                                     |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                     |
| scimark_monte_carlo     | 108 ms                                                 | 67.8 ms: 1.60x faster                                                    |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.59x faster                                                    |
| hexiom                  | 9.53 ms                                                | 6.02 ms: 1.58x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 33.2 us: 1.58x faster                                                    |
| mako                    | 14.8 ms                                                | 9.37 ms: 1.57x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 75.8 ms: 1.56x faster                                                    |
| spectral_norm           | 150 ms                                                 | 97.1 ms: 1.54x faster                                                    |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                                    |
| unpack_sequence         | 64.7 ns                                                | 42.6 ns: 1.52x faster                                                    |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                     |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                    |
| nbody                   | 142 ms                                                 | 96.6 ms: 1.47x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 665 ms: 1.44x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                    |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                    |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                    |
| html5lib                | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                    |
| logging_simple          | 8.07 us                                                | 5.68 us: 1.42x faster                                                    |
| logging_format          | 8.91 us                                                | 6.28 us: 1.42x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                                    |
| xml_etree_process       | 74.9 ms                                                | 53.2 ms: 1.41x faster                                                    |
| chameleon               | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                    |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                     |
| thrift                  | 1.03 ms                                                | 763 us: 1.35x faster                                                     |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                    |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.33x faster                                                   |
| async_tree_none         | 717 ms                                                 | 541 ms: 1.33x faster                                                     |
| 2to3                    | 336 ms                                                 | 255 ms: 1.32x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.32x faster                                                    |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                    |
| coroutines              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                    |
| nqueens                 | 100 ms                                                 | 78.7 ms: 1.27x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 683 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 769 ms: 1.24x faster                                                     |
| xml_etree_generate      | 94.2 ms                                                | 76.3 ms: 1.24x faster                                                    |
| dulwich_log             | 75.9 ms                                                | 62.2 ms: 1.22x faster                                                    |
| bench_thread_pool       | 947 us                                                 | 780 us: 1.21x faster                                                     |
| async_generators        | 425 ms                                                 | 352 ms: 1.21x faster                                                     |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                    |
| docutils                | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                   |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.20x faster                                                     |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                                    |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                     |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                    |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.09 us: 1.11x faster                                                    |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                     |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                     |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.09x faster                                                     |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                     |
| json                    | 5.42 ms                                                | 5.17 ms: 1.05x faster                                                    |
| telco                   | 6.54 ms                                                | 6.31 ms: 1.04x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.73 sec: 1.04x faster                                                   |
| unpickle                | 14.1 us                                                | 13.8 us: 1.03x faster                                                    |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                    |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| unpickle_list           | 4.82 us                                                | 5.03 us: 1.04x slower                                                    |
| python_startup_no_site  | 5.82 ms                                                | 6.13 ms: 1.05x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                    |
| pickle_dict             | 27.3 us                                                | 30.4 us: 1.12x slower                                                    |
| coverage                | 72.8 ms                                                | 104 ms: 1.43x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, generators
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221222-3.12.0a3+-9e5a8e4/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
