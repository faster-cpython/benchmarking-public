
# Results vs. 3.10.4

- fork: faster-cpython
- ref: perf_perf
- machine: linux-x86_64
- commit hash: 2aab3df
- commit date: 2023-03-23
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 271 ms: 1.24x faster                                                  |
| chameleon      | 9.06 ms                                                | 7.07 ms: 1.28x faster                                                 |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                |
| html5lib       | 85.9 ms                                                | 68.3 ms: 1.26x faster                                                 |
| tornado_http   | 127 ms                                                 | 104 ms: 1.23x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.0 ms: 1.59x faster                                                 |
| float          | 111 ms                                                 | 79.0 ms: 1.40x faster                                                 |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                 |
| regex_dna      | 222 ms                                                 | 206 ms: 1.07x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                 |
| pickle_pure_python   | 455 us                                                 | 337 us: 1.35x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 238 us: 1.26x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 60.6 ms: 1.24x faster                                                 |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                 |
| pickle_list          | 4.56 us                                                | 4.10 us: 1.11x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                  |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                 |
| unpickle_list        | 4.82 us                                                | 5.20 us: 1.08x slower                                                 |
| pickle_dict          | 27.3 us                                                | 30.5 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.52 ms: 1.49x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.88 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                 |
| genshi_text     | 30.3 ms                                                | 24.5 ms: 1.24x faster                                                 |
| genshi_xml      | 63.3 ms                                                | 52.2 ms: 1.21x faster                                                 |
| django_template | 45.9 ms                                                | 39.1 ms: 1.17x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.61x faster                                                 |
| asyncio_tcp             | 925 ms                                                 | 522 ms: 1.77x faster                                                  |
| deltablue               | 7.42 ms                                                | 4.47 ms: 1.66x faster                                                 |
| nbody                   | 142 ms                                                 | 89.0 ms: 1.59x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.58x faster                                                 |
| scimark_sor             | 197 ms                                                 | 127 ms: 1.55x faster                                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 42.7 ns: 1.52x faster                                                 |
| chaos                   | 106 ms                                                 | 70.3 ms: 1.51x faster                                                 |
| scimark_monte_carlo     | 108 ms                                                 | 71.9 ms: 1.51x faster                                                 |
| python_startup          | 14.2 ms                                                | 9.52 ms: 1.49x faster                                                 |
| go                      | 229 ms                                                 | 161 ms: 1.42x faster                                                  |
| pyflate                 | 673 ms                                                 | 478 ms: 1.41x faster                                                  |
| scimark_fft             | 424 ms                                                 | 302 ms: 1.40x faster                                                  |
| float                   | 111 ms                                                 | 79.0 ms: 1.40x faster                                                 |
| spectral_norm           | 150 ms                                                 | 108 ms: 1.39x faster                                                  |
| mako                    | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                 |
| raytrace                | 464 ms                                                 | 337 ms: 1.38x faster                                                  |
| richards                | 74.9 ms                                                | 54.6 ms: 1.37x faster                                                 |
| pickle_pure_python      | 455 us                                                 | 337 us: 1.35x faster                                                  |
| logging_silent          | 175 ns                                                 | 130 ns: 1.35x faster                                                  |
| hexiom                  | 9.53 ms                                                | 7.09 ms: 1.34x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.14 ms: 1.32x faster                                                 |
| chameleon               | 9.06 ms                                                | 7.07 ms: 1.28x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 1.39 sec: 1.28x faster                                                |
| pycparser               | 1.50 sec                                               | 1.18 sec: 1.27x faster                                                |
| deepcopy_memo           | 52.3 us                                                | 41.2 us: 1.27x faster                                                 |
| aiohttp                 | 1.38 ms                                                | 1.09 ms: 1.27x faster                                                 |
| gunicorn                | 1.46 ms                                                | 1.16 ms: 1.26x faster                                                 |
| async_tree_none         | 717 ms                                                 | 568 ms: 1.26x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 238 us: 1.26x faster                                                  |
| html5lib                | 85.9 ms                                                | 68.3 ms: 1.26x faster                                                 |
| fannkuch                | 486 ms                                                 | 387 ms: 1.26x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 684 ms: 1.25x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.59 sec: 1.25x faster                                                |
| thrift                  | 1.03 ms                                                | 830 us: 1.25x faster                                                  |
| 2to3                    | 336 ms                                                 | 271 ms: 1.24x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 770 ms: 1.24x faster                                                  |
| genshi_text             | 30.3 ms                                                | 24.5 ms: 1.24x faster                                                 |
| sqlglot_parse           | 2.06 ms                                                | 1.66 ms: 1.24x faster                                                 |
| xml_etree_process       | 74.9 ms                                                | 60.6 ms: 1.24x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.99 ms: 1.23x faster                                                 |
| tornado_http            | 127 ms                                                 | 104 ms: 1.23x faster                                                  |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 52.2 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 793 ms: 1.20x faster                                                  |
| nqueens                 | 100 ms                                                 | 84.6 ms: 1.18x faster                                                 |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                 |
| django_template         | 45.9 ms                                                | 39.1 ms: 1.17x faster                                                 |
| deepcopy                | 442 us                                                 | 377 us: 1.17x faster                                                  |
| docutils                | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                                 |
| deepcopy_reduce         | 3.82 us                                                | 3.35 us: 1.14x faster                                                 |
| coroutines              | 31.8 ms                                                | 28.0 ms: 1.14x faster                                                 |
| mypy2                   | 428 ms                                                 | 378 ms: 1.13x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 837 us: 1.13x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                 |
| xml_etree_generate      | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 121 ms: 1.12x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 58.5 ms: 1.12x faster                                                 |
| sqlalchemy_declarative  | 165 ms                                                 | 148 ms: 1.11x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.10 us: 1.11x faster                                                 |
| regex_v8                | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                 |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.5 ms: 1.09x faster                                                 |
| sympy_expand            | 545 ms                                                 | 501 ms: 1.09x faster                                                  |
| logging_format          | 8.91 us                                                | 8.20 us: 1.09x faster                                                 |
| dulwich_log             | 75.9 ms                                                | 69.9 ms: 1.09x faster                                                 |
| sympy_integrate         | 24.3 ms                                                | 22.4 ms: 1.08x faster                                                 |
| logging_simple          | 8.07 us                                                | 7.48 us: 1.08x faster                                                 |
| djangocms               | 35.9 us                                                | 33.4 us: 1.08x faster                                                 |
| regex_dna               | 222 ms                                                 | 206 ms: 1.07x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.65 sec: 1.06x faster                                                |
| sympy_str               | 328 ms                                                 | 311 ms: 1.06x faster                                                  |
| pathlib                 | 20.0 ms                                                | 19.0 ms: 1.05x faster                                                 |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                 |
| comprehensions          | 26.8 us                                                | 26.0 us: 1.03x faster                                                 |
| sympy_sum               | 185 ms                                                 | 179 ms: 1.03x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| async_generators        | 425 ms                                                 | 436 ms: 1.03x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                 |
| unpickle_list           | 4.82 us                                                | 5.20 us: 1.08x slower                                                 |
| pickle_dict             | 27.3 us                                                | 30.5 us: 1.12x slower                                                 |
| gc_traversal            | 3.84 ms                                                | 4.32 ms: 1.13x slower                                                 |
| python_startup_no_site  | 5.82 ms                                                | 6.88 ms: 1.18x slower                                                 |
| dask                    | 423 ms                                                 | 557 ms: 1.32x slower                                                  |
| coverage                | 72.8 ms                                                | 103 ms: 1.41x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (3): pickle, bench_mp_pool, telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x
