
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b3
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 256 ms: 1.31x faster                                       |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                      |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                     |
| html5lib       | 85.9 ms                                                | 62.8 ms: 1.37x faster                                      |
| tornado_http   | 127 ms                                                 | 94.7 ms: 1.35x faster                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 111 ms                                                 | 73.9 ms: 1.50x faster                                      |
| nbody          | 142 ms                                                 | 94.9 ms: 1.49x faster                                      |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                       |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                      |
| regex_dna      | 222 ms                                                 | 194 ms: 1.14x faster                                       |
| regex_effbot   | 3.23 ms                                                | 2.92 ms: 1.11x faster                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 301 us: 1.51x faster                                       |
| xml_etree_process    | 74.9 ms                                                | 53.6 ms: 1.40x faster                                      |
| unpickle_pure_python | 300 us                                                 | 227 us: 1.32x faster                                       |
| xml_etree_generate   | 94.2 ms                                                | 76.7 ms: 1.23x faster                                      |
| json_loads           | 28.8 us                                                | 24.9 us: 1.16x faster                                      |
| pickle               | 10.3 us                                                | 9.37 us: 1.10x faster                                      |
| json_dumps           | 13.5 ms                                                | 12.7 ms: 1.07x faster                                      |
| pickle_list          | 4.56 us                                                | 4.27 us: 1.07x faster                                      |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                      |
| pickle_dict          | 27.3 us                                                | 26.0 us: 1.05x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 108 ms: 1.04x faster                                       |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                       |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                      |
| Geometric mean       | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.51 ms: 1.66x faster                                      |
| python_startup_no_site | 5.82 ms                                                | 6.01 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.99 ms: 1.48x faster                                      |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                      |
| genshi_text     | 30.3 ms                                                | 22.0 ms: 1.38x faster                                      |
| genshi_xml      | 63.3 ms                                                | 52.3 ms: 1.21x faster                                      |
| Geometric mean  | (ref)                                                  | 1.36x faster                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.65 ms: 2.03x faster                                      |
| logging_silent          | 175 ns                                                 | 101 ns: 1.73x faster                                       |
| scimark_sor             | 197 ms                                                 | 114 ms: 1.72x faster                                       |
| python_startup          | 14.2 ms                                                | 8.51 ms: 1.66x faster                                      |
| richards                | 74.9 ms                                                | 45.3 ms: 1.65x faster                                      |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                       |
| pyflate                 | 673 ms                                                 | 409 ms: 1.65x faster                                       |
| scimark_monte_carlo     | 108 ms                                                 | 66.6 ms: 1.63x faster                                      |
| crypto_pyaes            | 118 ms                                                 | 73.6 ms: 1.61x faster                                      |
| raytrace                | 464 ms                                                 | 292 ms: 1.59x faster                                       |
| chaos                   | 106 ms                                                 | 68.2 ms: 1.56x faster                                      |
| spectral_norm           | 150 ms                                                 | 97.5 ms: 1.54x faster                                      |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                       |
| pickle_pure_python      | 455 us                                                 | 301 us: 1.51x faster                                       |
| hexiom                  | 9.53 ms                                                | 6.36 ms: 1.50x faster                                      |
| float                   | 111 ms                                                 | 73.9 ms: 1.50x faster                                      |
| nbody                   | 142 ms                                                 | 94.9 ms: 1.49x faster                                      |
| mako                    | 14.8 ms                                                | 9.99 ms: 1.48x faster                                      |
| deepcopy_memo           | 52.3 us                                                | 36.9 us: 1.42x faster                                      |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                      |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                      |
| xml_etree_process       | 74.9 ms                                                | 53.6 ms: 1.40x faster                                      |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                      |
| logging_simple          | 8.07 us                                                | 5.82 us: 1.39x faster                                      |
| pprint_safe_repr        | 955 ms                                                 | 694 ms: 1.38x faster                                       |
| genshi_text             | 30.3 ms                                                | 22.0 ms: 1.38x faster                                      |
| pprint_pformat          | 1.99 sec                                               | 1.45 sec: 1.37x faster                                     |
| html5lib                | 85.9 ms                                                | 62.8 ms: 1.37x faster                                      |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.36x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                     |
| thrift                  | 1.03 ms                                                | 763 us: 1.35x faster                                       |
| unpack_sequence         | 64.7 ns                                                | 48.0 ns: 1.35x faster                                      |
| tornado_http            | 127 ms                                                 | 94.7 ms: 1.35x faster                                      |
| async_tree_memoization  | 854 ms                                                 | 636 ms: 1.34x faster                                       |
| unpickle_pure_python    | 300 us                                                 | 227 us: 1.32x faster                                       |
| 2to3                    | 336 ms                                                 | 256 ms: 1.31x faster                                       |
| aiohttp                 | 1.38 ms                                                | 1.06 ms: 1.30x faster                                      |
| gunicorn                | 1.46 ms                                                | 1.12 ms: 1.30x faster                                      |
| deepcopy                | 442 us                                                 | 340 us: 1.30x faster                                       |
| regex_compile           | 177 ms                                                 | 136 ms: 1.30x faster                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 735 ms: 1.29x faster                                       |
| scimark_fft             | 424 ms                                                 | 328 ms: 1.29x faster                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.28x faster                                      |
| pycparser               | 1.50 sec                                               | 1.18 sec: 1.28x faster                                     |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.24x faster                                       |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                     |
| fannkuch                | 486 ms                                                 | 393 ms: 1.24x faster                                       |
| xml_etree_generate      | 94.2 ms                                                | 76.7 ms: 1.23x faster                                      |
| coroutines              | 31.8 ms                                                | 26.0 ms: 1.22x faster                                      |
| genshi_xml              | 63.3 ms                                                | 52.3 ms: 1.21x faster                                      |
| sqlglot_optimize        | 65.3 ms                                                | 54.0 ms: 1.21x faster                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                       |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.21x faster                                      |
| sqlglot_transpile       | 2.45 ms                                                | 2.04 ms: 1.20x faster                                      |
| async_generators        | 425 ms                                                 | 356 ms: 1.20x faster                                       |
| nqueens                 | 100 ms                                                 | 83.8 ms: 1.19x faster                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.57 ms: 1.19x faster                                      |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.8 ms: 1.19x faster                                      |
| flaskblogging           | 8.27 ms                                                | 7.04 ms: 1.18x faster                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.75 ms: 1.18x faster                                      |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                      |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                      |
| sympy_expand            | 545 ms                                                 | 469 ms: 1.16x faster                                       |
| bench_thread_pool       | 947 us                                                 | 816 us: 1.16x faster                                       |
| json_loads              | 28.8 us                                                | 24.9 us: 1.16x faster                                      |
| sqlite_synth            | 2.93 us                                                | 2.53 us: 1.16x faster                                      |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                       |
| dask                    | 423 ms                                                 | 368 ms: 1.15x faster                                       |
| regex_dna               | 222 ms                                                 | 194 ms: 1.14x faster                                       |
| json                    | 5.42 ms                                                | 4.74 ms: 1.14x faster                                      |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                       |
| pylint                  | 525 ms                                                 | 465 ms: 1.13x faster                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.51 ms: 1.11x faster                                      |
| regex_effbot            | 3.23 ms                                                | 2.92 ms: 1.11x faster                                      |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                      |
| pickle                  | 10.3 us                                                | 9.37 us: 1.10x faster                                      |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                       |
| djangocms               | 35.9 us                                                | 33.2 us: 1.08x faster                                      |
| json_dumps              | 13.5 ms                                                | 12.7 ms: 1.07x faster                                      |
| pickle_list             | 4.56 us                                                | 4.27 us: 1.07x faster                                      |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                      |
| pickle_dict             | 27.3 us                                                | 26.0 us: 1.05x faster                                      |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                     |
| asyncio_tcp             | 925 ms                                                 | 888 ms: 1.04x faster                                       |
| generators              | 76.8 ms                                                | 73.8 ms: 1.04x faster                                      |
| xml_etree_iterparse     | 111 ms                                                 | 108 ms: 1.04x faster                                       |
| comprehensions          | 26.8 us                                                | 25.9 us: 1.03x faster                                      |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.03x faster                                       |
| gc_traversal            | 3.84 ms                                                | 3.79 ms: 1.01x faster                                      |
| telco                   | 6.54 ms                                                | 6.59 ms: 1.01x slower                                      |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                       |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.01 ms: 1.03x slower                                      |
| Geometric mean          | (ref)                                                  | 1.26x faster                                               |

Benchmark hidden because not significant (2): mypy2, bench_mp_pool
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
