
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: 00b5a0c
- commit date: 2023-01-27
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.32x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                  |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| tornado_http   | 127 ms                                                 | 94.7 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.5 ms: 1.52x faster                                                  |
| nbody          | 142 ms                                                 | 94.8 ms: 1.49x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.37 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.50x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 77.8 ms: 1.21x faster                                                  |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.15 us: 1.10x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                                  |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                  |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.45 ms: 1.56x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                  |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.25 ms: 2.28x faster                                                  |
| logging_silent          | 175 ns                                                 | 92.0 ns: 1.90x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 498 ms: 1.86x faster                                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                   |
| richards                | 74.9 ms                                                | 42.4 ms: 1.77x faster                                                  |
| pyflate                 | 673 ms                                                 | 394 ms: 1.71x faster                                                   |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                   |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 73.1 ms: 1.62x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 67.1 ms: 1.61x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                   |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                                  |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.58x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                  |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                                  |
| mako                    | 14.8 ms                                                | 9.45 ms: 1.56x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 33.8 us: 1.55x faster                                                  |
| float                   | 111 ms                                                 | 72.5 ms: 1.52x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.50x faster                                                   |
| nbody                   | 142 ms                                                 | 94.8 ms: 1.49x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 43.8 ns: 1.48x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                  |
| scimark_lu              | 163 ms                                                 | 112 ms: 1.46x faster                                                   |
| json_dumps              | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                                   |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                  |
| async_tree_none         | 717 ms                                                 | 517 ms: 1.39x faster                                                   |
| logging_format          | 8.91 us                                                | 6.45 us: 1.38x faster                                                  |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                                   |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                   |
| logging_simple          | 8.07 us                                                | 5.87 us: 1.37x faster                                                  |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                                   |
| aiohttp                 | 1.38 ms                                                | 1.02 ms: 1.36x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                  |
| tornado_http            | 127 ms                                                 | 94.7 ms: 1.35x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                 |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                 |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                                   |
| 2to3                    | 336 ms                                                 | 254 ms: 1.32x faster                                                   |
| nqueens                 | 100 ms                                                 | 76.3 ms: 1.31x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                                  |
| fannkuch                | 486 ms                                                 | 381 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 747 ms: 1.27x faster                                                   |
| coroutines              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                  |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.26x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 52.1 ms: 1.25x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.0 ms: 1.22x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 62.7 ms: 1.21x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 77.8 ms: 1.21x faster                                                  |
| async_generators        | 425 ms                                                 | 352 ms: 1.21x faster                                                   |
| sympy_str               | 328 ms                                                 | 273 ms: 1.20x faster                                                   |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                                   |
| sympy_expand            | 545 ms                                                 | 461 ms: 1.18x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                  |
| json                    | 5.42 ms                                                | 4.78 ms: 1.13x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.41 ms: 1.13x faster                                                  |
| json_loads              | 28.8 us                                                | 25.7 us: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.15 us: 1.10x faster                                                  |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                                  |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                   |
| djangocms               | 35.9 us                                                | 33.5 us: 1.07x faster                                                  |
| telco                   | 6.54 ms                                                | 6.25 ms: 1.05x faster                                                  |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.66 ms: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| generators              | 76.8 ms                                                | 78.4 ms: 1.02x slower                                                  |
| unpickle_list           | 4.82 us                                                | 4.95 us: 1.03x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.37 ms: 1.04x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.3 us: 1.15x slower                                                  |
| dask                    | 423 ms                                                 | 518 ms: 1.23x slower                                                   |
| bench_mp_pool           | 24.0 ms                                                | 30.6 ms: 1.27x slower                                                  |
| coverage                | 72.8 ms                                                | 99.4 ms: 1.37x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230127-3.12.0a4+-00b5a0c/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
