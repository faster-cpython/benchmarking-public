
# Results vs. 3.10.4

- fork: iritkatriel
- ref: copy_consts
- machine: linux-x86_64
- commit hash: f8449d5
- commit date: 2023-01-18
- overall geometric mean: 1.28x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 257 ms: 1.31x faster                                               |
| chameleon      | 9.06 ms                                                | 6.53 ms: 1.39x faster                                              |
| docutils       | 3.17 sec                                               | 2.59 sec: 1.22x faster                                             |
| html5lib       | 85.9 ms                                                | 61.5 ms: 1.40x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.4 ms: 1.52x faster                                              |
| float          | 111 ms                                                 | 73.5 ms: 1.50x faster                                              |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.32x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                               |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                              |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.41 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.13x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.55x faster                                               |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.65 ms: 1.40x faster                                              |
| xml_etree_process    | 74.9 ms                                                | 54.6 ms: 1.37x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 78.6 ms: 1.20x faster                                              |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                              |
| pickle_list          | 4.56 us                                                | 4.03 us: 1.13x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                              |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                              |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.56 ms: 1.65x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.10 ms: 1.05x slower                                              |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.67 ms: 1.53x faster                                              |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                              |
| django_template | 45.9 ms                                                | 33.8 ms: 1.36x faster                                              |
| genshi_xml      | 63.3 ms                                                | 48.1 ms: 1.32x faster                                              |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.38 ms: 2.20x faster                                              |
| logging_silent          | 175 ns                                                 | 95.0 ns: 1.84x faster                                              |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 511 ms: 1.81x faster                                               |
| richards                | 74.9 ms                                                | 43.8 ms: 1.71x faster                                              |
| pyflate                 | 673 ms                                                 | 406 ms: 1.66x faster                                               |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                               |
| python_startup          | 14.2 ms                                                | 8.56 ms: 1.65x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 67.4 ms: 1.61x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.58x faster                                              |
| raytrace                | 464 ms                                                 | 293 ms: 1.58x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 41.6 ns: 1.55x faster                                              |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.55x faster                                               |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.55x faster                                              |
| hexiom                  | 9.53 ms                                                | 6.18 ms: 1.54x faster                                              |
| mako                    | 14.8 ms                                                | 9.67 ms: 1.53x faster                                              |
| nbody                   | 142 ms                                                 | 93.4 ms: 1.52x faster                                              |
| spectral_norm           | 150 ms                                                 | 99.0 ms: 1.52x faster                                              |
| float                   | 111 ms                                                 | 73.5 ms: 1.50x faster                                              |
| deepcopy_memo           | 52.3 us                                                | 35.1 us: 1.49x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                               |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                               |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.65 ms: 1.40x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                             |
| html5lib                | 85.9 ms                                                | 61.5 ms: 1.40x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.39x faster                                              |
| chameleon               | 9.06 ms                                                | 6.53 ms: 1.39x faster                                              |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 54.6 ms: 1.37x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 700 ms: 1.37x faster                                               |
| django_template         | 45.9 ms                                                | 33.8 ms: 1.36x faster                                              |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                             |
| async_tree_none         | 717 ms                                                 | 530 ms: 1.35x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                              |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                               |
| logging_format          | 8.91 us                                                | 6.66 us: 1.34x faster                                              |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                               |
| logging_simple          | 8.07 us                                                | 6.06 us: 1.33x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.34 sec: 1.33x faster                                             |
| fannkuch                | 486 ms                                                 | 367 ms: 1.33x faster                                               |
| genshi_xml              | 63.3 ms                                                | 48.1 ms: 1.32x faster                                              |
| 2to3                    | 336 ms                                                 | 257 ms: 1.31x faster                                               |
| deepcopy                | 442 us                                                 | 341 us: 1.30x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.27x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 674 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 757 ms: 1.26x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.25x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 52.5 ms: 1.25x faster                                              |
| coroutines              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                              |
| docutils                | 3.17 sec                                               | 2.59 sec: 1.22x faster                                             |
| nqueens                 | 100 ms                                                 | 81.8 ms: 1.22x faster                                              |
| xml_etree_generate      | 94.2 ms                                                | 78.6 ms: 1.20x faster                                              |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                              |
| dulwich_log             | 75.9 ms                                                | 63.4 ms: 1.20x faster                                              |
| bench_thread_pool       | 947 us                                                 | 797 us: 1.19x faster                                               |
| async_generators        | 425 ms                                                 | 358 ms: 1.19x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                              |
| sympy_expand            | 545 ms                                                 | 469 ms: 1.16x faster                                               |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.15x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                              |
| sympy_str               | 328 ms                                                 | 288 ms: 1.14x faster                                               |
| pickle_list             | 4.56 us                                                | 4.03 us: 1.13x faster                                              |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.12x faster                                             |
| sympy_integrate         | 24.3 ms                                                | 21.9 ms: 1.11x faster                                              |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.10x faster                                               |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                               |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                              |
| djangocms               | 35.9 us                                                | 32.8 us: 1.09x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                              |
| telco                   | 6.54 ms                                                | 6.31 ms: 1.04x faster                                              |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| generators              | 76.8 ms                                                | 79.0 ms: 1.03x slower                                              |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.10 ms: 1.05x slower                                              |
| regex_effbot            | 3.23 ms                                                | 3.41 ms: 1.06x slower                                              |
| gc_traversal            | 3.84 ms                                                | 4.30 ms: 1.12x slower                                              |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                              |
| dask                    | 423 ms                                                 | 516 ms: 1.22x slower                                               |
| coverage                | 72.8 ms                                                | 98.3 ms: 1.35x slower                                              |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-f8449d5/bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x
