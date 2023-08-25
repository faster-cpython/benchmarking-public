
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 255 ms: 1.32x faster                                   |
| chameleon      | 9.06 ms                                                | 6.41 ms: 1.41x faster                                  |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                  |
| nbody          | 142 ms                                                 | 96.7 ms: 1.46x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.8 ms: 1.20x faster                                  |
| regex_dna      | 222 ms                                                 | 189 ms: 1.17x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.17 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                   |
| unpickle_pure_python | 300 us                                                 | 210 us: 1.43x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.4 ms: 1.40x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 78.2 ms: 1.20x faster                                  |
| json_loads           | 28.8 us                                                | 26.1 us: 1.11x faster                                  |
| pickle_list          | 4.56 us                                                | 4.14 us: 1.10x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.51 ms: 1.66x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.09 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.54 ms: 1.55x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                  |
| django_template | 45.9 ms                                                | 32.9 ms: 1.39x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.4 ms: 1.33x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.25 ms: 2.28x faster                                  |
| logging_silent          | 175 ns                                                 | 94.1 ns: 1.86x faster                                  |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                   |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                  |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.6 ms: 1.68x faster                                  |
| pyflate                 | 673 ms                                                 | 402 ms: 1.68x faster                                   |
| python_startup          | 14.2 ms                                                | 8.51 ms: 1.66x faster                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                   |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                   |
| hexiom                  | 9.53 ms                                                | 6.06 ms: 1.57x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 33.6 us: 1.56x faster                                  |
| mako                    | 14.8 ms                                                | 9.54 ms: 1.55x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 77.2 ms: 1.53x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 42.4 ns: 1.53x faster                                  |
| spectral_norm           | 150 ms                                                 | 98.6 ms: 1.52x faster                                  |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                  |
| chaos                   | 106 ms                                                 | 70.2 ms: 1.51x faster                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                  |
| nbody                   | 142 ms                                                 | 96.7 ms: 1.46x faster                                  |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                  |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 210 us: 1.43x faster                                   |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                 |
| chameleon               | 9.06 ms                                                | 6.41 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.4 ms: 1.40x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 681 ms: 1.40x faster                                   |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                  |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.39x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| thrift                  | 1.03 ms                                                | 757 us: 1.36x faster                                   |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                   |
| async_tree_none         | 717 ms                                                 | 536 ms: 1.34x faster                                   |
| genshi_xml              | 63.3 ms                                                | 47.4 ms: 1.33x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.33x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.11 ms: 1.33x faster                                  |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                 |
| 2to3                    | 336 ms                                                 | 255 ms: 1.32x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                  |
| scimark_fft             | 424 ms                                                 | 325 ms: 1.30x faster                                   |
| fannkuch                | 486 ms                                                 | 376 ms: 1.29x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 672 ms: 1.27x faster                                   |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| sqlglot_optimize        | 65.3 ms                                                | 51.7 ms: 1.26x faster                                  |
| coroutines              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 107 ms: 1.26x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 757 ms: 1.26x faster                                   |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.24x faster                                  |
| bench_thread_pool       | 947 us                                                 | 781 us: 1.21x faster                                   |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 78.2 ms: 1.20x faster                                  |
| regex_v8                | 25.0 ms                                                | 20.8 ms: 1.20x faster                                  |
| async_generators        | 425 ms                                                 | 356 ms: 1.19x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                   |
| regex_dna               | 222 ms                                                 | 189 ms: 1.17x faster                                   |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                   |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                  |
| json_loads              | 28.8 us                                                | 26.1 us: 1.11x faster                                  |
| pickle_list             | 4.56 us                                                | 4.14 us: 1.10x faster                                  |
| json                    | 5.42 ms                                                | 4.92 ms: 1.10x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                   |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                   |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| mdp                     | 2.82 sec                                               | 2.63 sec: 1.07x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| telco                   | 6.54 ms                                                | 6.36 ms: 1.03x faster                                  |
| regex_effbot            | 3.23 ms                                                | 3.17 ms: 1.02x faster                                  |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| generators              | 76.8 ms                                                | 76.2 ms: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.09 ms: 1.05x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.5 us: 1.16x slower                                  |
| coverage                | 72.8 ms                                                | 99.3 ms: 1.36x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230107-3.12.0a3+-951303f/bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
