
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: f58631b
- commit date: 2022-10-22
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.60 ms: 1.37x faster                                  |
| html5lib       | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| tornado_http   | 127 ms                                                 | 93.1 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.5 ms: 1.52x faster                                  |
| nbody          | 142 ms                                                 | 93.9 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                  |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 289 us: 1.58x faster                                   |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.49 ms: 1.43x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.1 ms: 1.41x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.5 ms: 1.25x faster                                  |
| json_loads           | 28.8 us                                                | 23.5 us: 1.23x faster                                  |
| pickle_list          | 4.56 us                                                | 3.96 us: 1.15x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.3 us: 1.07x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.37 ms: 1.69x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.06 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.75 ms: 1.51x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.45x faster                                  |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| genshi_xml      | 63.3 ms                                                | 49.7 ms: 1.27x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.30 ms: 2.25x faster                                  |
| logging_silent          | 175 ns                                                 | 90.5 ns: 1.94x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| richards                | 74.9 ms                                                | 43.5 ms: 1.72x faster                                  |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                   |
| python_startup          | 14.2 ms                                                | 8.37 ms: 1.69x faster                                  |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.6 ms: 1.63x faster                                  |
| raytrace                | 464 ms                                                 | 287 ms: 1.62x faster                                   |
| spectral_norm           | 150 ms                                                 | 95.1 ms: 1.58x faster                                  |
| pickle_pure_python      | 455 us                                                 | 289 us: 1.58x faster                                   |
| hexiom                  | 9.53 ms                                                | 6.07 ms: 1.57x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 76.4 ms: 1.55x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.54x faster                                  |
| chaos                   | 106 ms                                                 | 69.7 ms: 1.53x faster                                  |
| float                   | 111 ms                                                 | 72.5 ms: 1.52x faster                                  |
| mako                    | 14.8 ms                                                | 9.75 ms: 1.51x faster                                  |
| nbody                   | 142 ms                                                 | 93.9 ms: 1.51x faster                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.50x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                   |
| html5lib                | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                 |
| json_dumps              | 13.5 ms                                                | 9.49 ms: 1.43x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.1 ms: 1.41x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 678 ms: 1.41x faster                                   |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                   |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                 |
| logging_simple          | 8.07 us                                                | 5.84 us: 1.38x faster                                  |
| logging_format          | 8.91 us                                                | 6.47 us: 1.38x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.38x faster                                  |
| chameleon               | 9.06 ms                                                | 6.60 ms: 1.37x faster                                  |
| tornado_http            | 127 ms                                                 | 93.1 ms: 1.37x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| async_tree_none         | 717 ms                                                 | 530 ms: 1.35x faster                                   |
| 2to3                    | 336 ms                                                 | 250 ms: 1.35x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                 |
| scimark_fft             | 424 ms                                                 | 317 ms: 1.34x faster                                   |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 48.7 ns: 1.33x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.89 us: 1.32x faster                                  |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                   |
| coroutines              | 31.8 ms                                                | 24.4 ms: 1.30x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 732 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.22 ms: 1.29x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.28x faster                                   |
| genshi_xml              | 63.3 ms                                                | 49.7 ms: 1.27x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.5 ms: 1.25x faster                                  |
| nqueens                 | 100 ms                                                 | 80.3 ms: 1.25x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.3 ms: 1.24x faster                                  |
| json_loads              | 28.8 us                                                | 23.5 us: 1.23x faster                                  |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.19x faster                                  |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                   |
| pylint                  | 525 ms                                                 | 455 ms: 1.15x faster                                   |
| pickle_list             | 4.56 us                                                | 3.96 us: 1.15x faster                                  |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                 |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.7 ms: 1.10x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| generators              | 76.8 ms                                                | 70.6 ms: 1.09x faster                                  |
| unpickle                | 14.1 us                                                | 13.3 us: 1.07x faster                                  |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                   |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.06 ms: 1.04x slower                                  |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| regex_effbot            | 3.23 ms                                                | 3.66 ms: 1.13x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                  |
| coverage                | 72.8 ms                                                | 97.8 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (2): telco, pickle
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221022-3.12.0a1+-f58631b/bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x
