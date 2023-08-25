
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: f23eec9
- commit date: 2023-01-27
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.28 ms: 1.44x faster                                                  |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                  |
| tornado_http   | 127 ms                                                 | 93.9 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.7 ms: 1.54x faster                                                  |
| nbody          | 142 ms                                                 | 94.0 ms: 1.51x faster                                                  |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| regex_v8       | 25.0 ms                                                | 26.0 ms: 1.04x slower                                                  |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.40x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 77.3 ms: 1.22x faster                                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.03 us: 1.13x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                  |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                  |
| unpickle_list        | 4.82 us                                                | 5.04 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.45 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.71 ms: 1.52x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                                  |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 498 ms: 1.86x faster                                                   |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                   |
| logging_silent          | 175 ns                                                 | 94.9 ns: 1.85x faster                                                  |
| richards                | 74.9 ms                                                | 42.5 ms: 1.76x faster                                                  |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                                   |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                                   |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.8 ms: 1.64x faster                                                  |
| chaos                   | 106 ms                                                 | 64.9 ms: 1.64x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 73.0 ms: 1.62x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                                   |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.00 ms: 1.59x faster                                                  |
| float                   | 111 ms                                                 | 71.7 ms: 1.54x faster                                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                                   |
| mako                    | 14.8 ms                                                | 9.71 ms: 1.52x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                   |
| nbody                   | 142 ms                                                 | 94.0 ms: 1.51x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 34.8 us: 1.51x faster                                                  |
| spectral_norm           | 150 ms                                                 | 100 ms: 1.50x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 44.0 ns: 1.47x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.28 ms: 1.44x faster                                                  |
| logging_format          | 8.91 us                                                | 6.19 us: 1.44x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.62 us: 1.44x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                 |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 678 ms: 1.41x faster                                                   |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                                  |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.40x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 995 us: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.06 ms: 1.37x faster                                                  |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                  |
| tornado_http            | 127 ms                                                 | 93.9 ms: 1.36x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                 |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                                   |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| deepcopy                | 442 us                                                 | 334 us: 1.32x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 645 ms: 1.32x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                 |
| nqueens                 | 100 ms                                                 | 76.3 ms: 1.31x faster                                                  |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.29x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                                  |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 758 ms: 1.25x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 776 us: 1.22x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 77.3 ms: 1.22x faster                                                  |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 62.6 ms: 1.21x faster                                                  |
| async_generators        | 425 ms                                                 | 352 ms: 1.21x faster                                                   |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                   |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                  |
| json                    | 5.42 ms                                                | 4.56 ms: 1.19x faster                                                  |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.03 us: 1.13x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                 |
| djangocms               | 35.9 us                                                | 32.8 us: 1.10x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                  |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| telco                   | 6.54 ms                                                | 6.39 ms: 1.02x faster                                                  |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                  |
| generators              | 76.8 ms                                                | 77.4 ms: 1.01x slower                                                  |
| regex_v8                | 25.0 ms                                                | 26.0 ms: 1.04x slower                                                  |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| unpickle_list           | 4.82 us                                                | 5.04 us: 1.05x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.45 ms: 1.11x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 4.29 ms: 1.12x slower                                                  |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                  |
| dask                    | 423 ms                                                 | 494 ms: 1.17x slower                                                   |
| coverage                | 72.8 ms                                                | 97.2 ms: 1.34x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230127-3.12.0a4+-f23eec9/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
