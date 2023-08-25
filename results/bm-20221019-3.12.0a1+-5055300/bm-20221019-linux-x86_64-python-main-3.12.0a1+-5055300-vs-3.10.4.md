
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5055300
- commit date: 2022-10-19
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.46 ms: 1.40x faster                                  |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| tornado_http   | 127 ms                                                 | 93.0 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 71.1 ms: 1.55x faster                                  |
| nbody          | 142 ms                                                 | 94.8 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                   |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.44x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.3 ms: 1.40x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.9 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.56 us                                                | 3.99 us: 1.14x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 144 ms: 1.13x faster                                   |
| unpickle             | 14.1 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.32 ms: 1.70x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.03 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.79 ms: 1.51x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                  |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                  |
| genshi_xml      | 63.3 ms                                                | 49.3 ms: 1.28x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.36 ms: 2.21x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| logging_silent          | 175 ns                                                 | 93.3 ns: 1.88x faster                                  |
| python_startup          | 14.2 ms                                                | 8.32 ms: 1.70x faster                                  |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                   |
| richards                | 74.9 ms                                                | 45.2 ms: 1.66x faster                                  |
| pyflate                 | 673 ms                                                 | 409 ms: 1.65x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 67.0 ms: 1.62x faster                                  |
| raytrace                | 464 ms                                                 | 289 ms: 1.60x faster                                   |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                   |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 75.4 ms: 1.57x faster                                  |
| chaos                   | 106 ms                                                 | 67.8 ms: 1.57x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                  |
| float                   | 111 ms                                                 | 71.1 ms: 1.55x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                  |
| mako                    | 14.8 ms                                                | 9.79 ms: 1.51x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.51x faster                                  |
| nbody                   | 142 ms                                                 | 94.8 ms: 1.49x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                   |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.44x faster                                 |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.44x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 669 ms: 1.43x faster                                   |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 45.7 ns: 1.42x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.3 ms: 1.40x faster                                  |
| chameleon               | 9.06 ms                                                | 6.46 ms: 1.40x faster                                  |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                   |
| logging_simple          | 8.07 us                                                | 5.83 us: 1.38x faster                                  |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.38x faster                                 |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| logging_format          | 8.91 us                                                | 6.49 us: 1.37x faster                                  |
| tornado_http            | 127 ms                                                 | 93.0 ms: 1.37x faster                                  |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                   |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.36x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                 |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                  |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                   |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.89 us: 1.32x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.31x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 657 ms: 1.30x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 732 ms: 1.30x faster                                   |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                  |
| genshi_xml              | 63.3 ms                                                | 49.3 ms: 1.28x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.2 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.9 ms: 1.23x faster                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                  |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.20x faster                                   |
| sympy_str               | 328 ms                                                 | 280 ms: 1.17x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                  |
| pylint                  | 525 ms                                                 | 454 ms: 1.16x faster                                   |
| pickle_list             | 4.56 us                                                | 3.99 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| json                    | 5.42 ms                                                | 4.77 ms: 1.14x faster                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                   |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.13x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 144 ms: 1.13x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                  |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| generators              | 76.8 ms                                                | 71.4 ms: 1.08x faster                                  |
| unpickle                | 14.1 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                 |
| telco                   | 6.54 ms                                                | 6.43 ms: 1.02x faster                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.03 ms: 1.04x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| coverage                | 72.8 ms                                                | 97.7 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221019-3.12.0a1+-5055300/bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x
