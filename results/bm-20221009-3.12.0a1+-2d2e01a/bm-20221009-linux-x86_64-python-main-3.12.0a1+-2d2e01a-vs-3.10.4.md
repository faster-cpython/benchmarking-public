
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d2e01a
- commit date: 2022-10-09
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.36x faster                                   |
| chameleon      | 9.06 ms                                                | 6.61 ms: 1.37x faster                                  |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| tornado_http   | 127 ms                                                 | 93.4 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.3 ms: 1.53x faster                                  |
| nbody          | 142 ms                                                 | 94.6 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.55x faster                                   |
| unpickle_pure_python | 300 us                                                 | 204 us: 1.47x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.40x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.6 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                  |
| pickle_list          | 4.56 us                                                | 4.06 us: 1.12x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.38 ms: 1.69x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.06 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.84 ms: 1.50x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                  |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                  |
| genshi_xml      | 63.3 ms                                                | 49.1 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.40 ms: 2.18x faster                                  |
| logging_silent          | 175 ns                                                 | 92.7 ns: 1.89x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| python_startup          | 14.2 ms                                                | 8.38 ms: 1.69x faster                                  |
| richards                | 74.9 ms                                                | 44.4 ms: 1.69x faster                                  |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                   |
| pyflate                 | 673 ms                                                 | 407 ms: 1.66x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.3 ms: 1.63x faster                                  |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                   |
| chaos                   | 106 ms                                                 | 65.5 ms: 1.62x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.02 ms: 1.58x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 75.3 ms: 1.57x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.4 ms: 1.56x faster                                  |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.55x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.53x faster                                  |
| float                   | 111 ms                                                 | 72.3 ms: 1.53x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.52x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                   |
| mako                    | 14.8 ms                                                | 9.84 ms: 1.50x faster                                  |
| nbody                   | 142 ms                                                 | 94.6 ms: 1.50x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.64 ms: 1.49x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 204 us: 1.47x faster                                   |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                 |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                  |
| thrift                  | 1.03 ms                                                | 737 us: 1.40x faster                                   |
| pprint_safe_repr        | 955 ms                                                 | 682 ms: 1.40x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.40x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                  |
| logging_format          | 8.91 us                                                | 6.43 us: 1.39x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                  |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                 |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                  |
| chameleon               | 9.06 ms                                                | 6.61 ms: 1.37x faster                                  |
| tornado_http            | 127 ms                                                 | 93.4 ms: 1.36x faster                                  |
| 2to3                    | 336 ms                                                 | 248 ms: 1.36x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                  |
| async_tree_none         | 717 ms                                                 | 530 ms: 1.35x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                 |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                   |
| scimark_fft             | 424 ms                                                 | 316 ms: 1.34x faster                                   |
| deepcopy                | 442 us                                                 | 331 us: 1.34x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 731 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 50.2 ns: 1.29x faster                                  |
| genshi_xml              | 63.3 ms                                                | 49.1 ms: 1.29x faster                                  |
| coroutines              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 79.2 ms: 1.26x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.1 ms: 1.24x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.6 ms: 1.23x faster                                  |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                  |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| sympy_str               | 328 ms                                                 | 280 ms: 1.17x faster                                   |
| pylint                  | 525 ms                                                 | 454 ms: 1.16x faster                                   |
| json                    | 5.42 ms                                                | 4.72 ms: 1.15x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                  |
| pickle_list             | 4.56 us                                                | 4.06 us: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                   |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                 |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                  |
| generators              | 76.8 ms                                                | 73.8 ms: 1.04x faster                                  |
| telco                   | 6.54 ms                                                | 6.32 ms: 1.04x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.06 ms: 1.04x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.60 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| coverage                | 72.8 ms                                                | 98.9 ms: 1.36x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221009-3.12.0a1+-2d2e01a/bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x
