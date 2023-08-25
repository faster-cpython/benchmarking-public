
# Results vs. 3.10.4

- fork: python
- ref: v3.11.2
- machine: linux-x86_64
- commit hash: 878ead1
- commit date: 2023-02-07
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 257 ms: 1.31x faster                                   |
| chameleon      | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 64.0 ms: 1.34x faster                                  |
| tornado_http   | 127 ms                                                 | 96.1 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.0 ms: 1.52x faster                                  |
| float          | 111 ms                                                 | 76.6 ms: 1.44x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.28x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| regex_dna      | 222 ms                                                 | 192 ms: 1.15x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.39 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 305 us: 1.49x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 53.8 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                 | 228 us: 1.32x faster                                   |
| xml_etree_generate   | 94.2 ms                                                | 76.5 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 26.2 us: 1.10x faster                                  |
| pickle_list          | 4.56 us                                                | 4.16 us: 1.10x faster                                  |
| json_dumps           | 13.5 ms                                                | 12.5 ms: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| pickle               | 10.3 us                                                | 10.00 us: 1.03x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.02x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.47 ms: 1.67x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 5.97 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.83 ms: 1.50x faster                                  |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                  |
| genshi_xml      | 63.3 ms                                                | 51.5 ms: 1.23x faster                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.68 ms: 2.02x faster                                  |
| logging_silent          | 175 ns                                                 | 99.8 ns: 1.75x faster                                  |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                   |
| python_startup          | 14.2 ms                                                | 8.47 ms: 1.67x faster                                  |
| richards                | 74.9 ms                                                | 45.6 ms: 1.64x faster                                  |
| go                      | 229 ms                                                 | 141 ms: 1.62x faster                                   |
| pyflate                 | 673 ms                                                 | 417 ms: 1.61x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.61x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 67.7 ms: 1.60x faster                                  |
| raytrace                | 464 ms                                                 | 291 ms: 1.59x faster                                   |
| chaos                   | 106 ms                                                 | 68.2 ms: 1.56x faster                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                   |
| spectral_norm           | 150 ms                                                 | 98.4 ms: 1.52x faster                                  |
| nbody                   | 142 ms                                                 | 93.0 ms: 1.52x faster                                  |
| mako                    | 14.8 ms                                                | 9.83 ms: 1.50x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.36 ms: 1.50x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.38 ms: 1.49x faster                                  |
| pickle_pure_python      | 455 us                                                 | 305 us: 1.49x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.47x faster                                  |
| float                   | 111 ms                                                 | 76.6 ms: 1.44x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 36.8 us: 1.42x faster                                  |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                  |
| chameleon               | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.8 ms: 1.39x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.45 sec: 1.37x faster                                 |
| logging_format          | 8.91 us                                                | 6.49 us: 1.37x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 697 ms: 1.37x faster                                   |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                 |
| async_tree_memoization  | 854 ms                                                 | 628 ms: 1.36x faster                                   |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                 |
| logging_simple          | 8.07 us                                                | 5.97 us: 1.35x faster                                  |
| html5lib                | 85.9 ms                                                | 64.0 ms: 1.34x faster                                  |
| thrift                  | 1.03 ms                                                | 770 us: 1.34x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 48.8 ns: 1.33x faster                                  |
| tornado_http            | 127 ms                                                 | 96.1 ms: 1.33x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.05 ms: 1.32x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 228 us: 1.32x faster                                   |
| 2to3                    | 336 ms                                                 | 257 ms: 1.31x faster                                   |
| scimark_fft             | 424 ms                                                 | 327 ms: 1.29x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.13 ms: 1.29x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 740 ms: 1.28x faster                                   |
| regex_compile           | 177 ms                                                 | 138 ms: 1.28x faster                                   |
| deepcopy                | 442 us                                                 | 348 us: 1.27x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.04 us: 1.26x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.25x faster                                   |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                 |
| coroutines              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                  |
| fannkuch                | 486 ms                                                 | 392 ms: 1.24x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 76.5 ms: 1.23x faster                                  |
| genshi_xml              | 63.3 ms                                                | 51.5 ms: 1.23x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 53.3 ms: 1.23x faster                                  |
| nqueens                 | 100 ms                                                 | 83.1 ms: 1.20x faster                                  |
| async_generators        | 425 ms                                                 | 357 ms: 1.19x faster                                   |
| dulwich_log             | 75.9 ms                                                | 63.7 ms: 1.19x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.46 us: 1.19x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.63 ms: 1.18x faster                                  |
| flaskblogging           | 8.27 ms                                                | 7.02 ms: 1.18x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 141 ms: 1.17x faster                                   |
| bench_thread_pool       | 947 us                                                 | 812 us: 1.17x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.2 ms: 1.17x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.8 ms: 1.17x faster                                  |
| sympy_expand            | 545 ms                                                 | 468 ms: 1.16x faster                                   |
| dask                    | 423 ms                                                 | 365 ms: 1.16x faster                                   |
| regex_dna               | 222 ms                                                 | 192 ms: 1.15x faster                                   |
| sympy_str               | 328 ms                                                 | 288 ms: 1.14x faster                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                   |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                  |
| pylint                  | 525 ms                                                 | 475 ms: 1.11x faster                                   |
| json_loads              | 28.8 us                                                | 26.2 us: 1.10x faster                                  |
| json                    | 5.42 ms                                                | 4.92 ms: 1.10x faster                                  |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| pickle_list             | 4.56 us                                                | 4.16 us: 1.10x faster                                  |
| json_dumps              | 13.5 ms                                                | 12.5 ms: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 884 ms: 1.05x faster                                   |
| generators              | 76.8 ms                                                | 74.1 ms: 1.04x faster                                  |
| pickle                  | 10.3 us                                                | 10.00 us: 1.03x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.02x faster                                   |
| mdp                     | 2.82 sec                                               | 2.77 sec: 1.02x faster                                 |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| telco                   | 6.54 ms                                                | 6.59 ms: 1.01x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.03x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 5.97 ms: 1.03x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.39 ms: 1.05x slower                                  |
| gc_traversal            | 3.84 ms                                                | 4.15 ms: 1.08x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.4 us: 1.15x slower                                  |
| coverage                | 72.8 ms                                                | 103 ms: 1.42x slower                                   |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): mypy2, bench_mp_pool
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
