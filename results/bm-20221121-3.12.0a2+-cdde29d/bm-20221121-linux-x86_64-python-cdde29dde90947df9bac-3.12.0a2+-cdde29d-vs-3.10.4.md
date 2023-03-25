
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.32x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 244 ms: 1.38x faster                                                   |
| chameleon      | 9.13 ms                                                             | 6.31 ms: 1.45x faster                                                  |
| docutils       | 3.19 sec                                                            | 2.48 sec: 1.29x faster                                                 |
| html5lib       | 86.4 ms                                                             | 59.1 ms: 1.46x faster                                                  |
| tornado_http   | 129 ms                                                              | 92.8 ms: 1.39x faster                                                  |
| Geometric mean | (ref)                                                               | 1.39x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 93.7 ms: 1.56x faster                                                  |
| float          | 110 ms                                                              | 73.1 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                              | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                               | 1.33x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 127 ms: 1.39x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 21.0 ms: 1.19x faster                                                  |
| regex_dna      | 213 ms                                                              | 209 ms: 1.02x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.55 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                               | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 281 us: 1.63x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 198 us: 1.51x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 9.51 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 52.8 ms: 1.42x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 76.3 ms: 1.24x faster                                                  |
| json_loads           | 29.3 us                                                             | 23.8 us: 1.23x faster                                                  |
| pickle_list          | 4.73 us                                                             | 3.97 us: 1.19x faster                                                  |
| xml_etree_parse      | 164 ms                                                              | 147 ms: 1.11x faster                                                   |
| unpickle             | 15.0 us                                                             | 13.6 us: 1.10x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 102 ms: 1.10x faster                                                   |
| pickle               | 10.2 us                                                             | 10.4 us: 1.01x slower                                                  |
| unpickle_list        | 4.94 us                                                             | 5.13 us: 1.04x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 31.3 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.20x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.48 ms: 1.67x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.12 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.26x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.56 ms: 1.54x faster                                                  |
| genshi_text     | 30.4 ms                                                             | 20.2 ms: 1.51x faster                                                  |
| django_template | 45.8 ms                                                             | 32.1 ms: 1.43x faster                                                  |
| genshi_xml      | 64.3 ms                                                             | 46.6 ms: 1.38x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.17 ms: 2.31x faster                                                  |
| scimark_sor             | 198 ms                                                              | 107 ms: 1.85x faster                                                   |
| richards                | 74.2 ms                                                             | 41.3 ms: 1.80x faster                                                  |
| logging_silent          | 169 ns                                                              | 94.1 ns: 1.80x faster                                                  |
| go                      | 226 ms                                                              | 133 ms: 1.69x faster                                                   |
| pyflate                 | 671 ms                                                              | 397 ms: 1.69x faster                                                   |
| raytrace                | 470 ms                                                              | 280 ms: 1.68x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                              | 65.0 ms: 1.67x faster                                                  |
| python_startup          | 14.1 ms                                                             | 8.48 ms: 1.67x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 281 us: 1.63x faster                                                   |
| chaos                   | 106 ms                                                              | 65.6 ms: 1.61x faster                                                  |
| spectral_norm           | 150 ms                                                              | 95.6 ms: 1.57x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.32 ms: 1.56x faster                                                  |
| nbody                   | 146 ms                                                              | 93.7 ms: 1.56x faster                                                  |
| crypto_pyaes            | 117 ms                                                              | 75.1 ms: 1.55x faster                                                  |
| mako                    | 14.7 ms                                                             | 9.56 ms: 1.54x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 6.18 ms: 1.54x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 33.8 us: 1.53x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.61 ms: 1.52x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 198 us: 1.51x faster                                                   |
| scimark_lu              | 160 ms                                                              | 106 ms: 1.51x faster                                                   |
| genshi_text             | 30.4 ms                                                             | 20.2 ms: 1.51x faster                                                  |
| float                   | 110 ms                                                              | 73.1 ms: 1.50x faster                                                  |
| html5lib                | 86.4 ms                                                             | 59.1 ms: 1.46x faster                                                  |
| logging_simple          | 8.21 us                                                             | 5.62 us: 1.46x faster                                                  |
| unpack_sequence         | 65.6 ns                                                             | 45.1 ns: 1.45x faster                                                  |
| chameleon               | 9.13 ms                                                             | 6.31 ms: 1.45x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.29 us: 1.44x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 9.51 ms: 1.44x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.07 sec: 1.43x faster                                                 |
| django_template         | 45.8 ms                                                             | 32.1 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.39 sec: 1.42x faster                                                 |
| xml_etree_process       | 74.8 ms                                                             | 52.8 ms: 1.42x faster                                                  |
| pprint_safe_repr        | 953 ms                                                              | 676 ms: 1.41x faster                                                   |
| regex_compile           | 177 ms                                                              | 127 ms: 1.39x faster                                                   |
| tornado_http            | 129 ms                                                              | 92.8 ms: 1.39x faster                                                  |
| thrift                  | 1.04 ms                                                             | 748 us: 1.39x faster                                                   |
| scimark_fft             | 425 ms                                                              | 307 ms: 1.38x faster                                                   |
| genshi_xml              | 64.3 ms                                                             | 46.6 ms: 1.38x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.08 ms: 1.38x faster                                                  |
| 2to3                    | 336 ms                                                              | 244 ms: 1.38x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 622 ms: 1.37x faster                                                   |
| aiohttp                 | 1.35 ms                                                             | 991 us: 1.36x faster                                                   |
| async_tree_none         | 713 ms                                                              | 530 ms: 1.35x faster                                                   |
| gunicorn                | 1.43 ms                                                             | 1.07 ms: 1.35x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.32 sec: 1.34x faster                                                 |
| deepcopy                | 438 us                                                              | 330 us: 1.33x faster                                                   |
| fannkuch                | 485 ms                                                              | 373 ms: 1.30x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 50.2 ms: 1.30x faster                                                  |
| coroutines              | 31.8 ms                                                             | 24.5 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.30x faster                                                   |
| docutils                | 3.19 sec                                                            | 2.48 sec: 1.29x faster                                                 |
| deepcopy_reduce         | 3.80 us                                                             | 2.99 us: 1.27x faster                                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 755 ms: 1.25x faster                                                   |
| xml_etree_generate      | 94.9 ms                                                             | 76.3 ms: 1.24x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 61.5 ms: 1.24x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 774 us: 1.23x faster                                                   |
| json_loads              | 29.3 us                                                             | 23.8 us: 1.23x faster                                                  |
| nqueens                 | 98.8 ms                                                             | 82.0 ms: 1.21x faster                                                  |
| sympy_integrate         | 24.3 ms                                                             | 20.3 ms: 1.20x faster                                                  |
| pickle_list             | 4.73 us                                                             | 3.97 us: 1.19x faster                                                  |
| sympy_expand            | 540 ms                                                              | 454 ms: 1.19x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 21.0 ms: 1.19x faster                                                  |
| async_generators        | 420 ms                                                              | 358 ms: 1.17x faster                                                   |
| json                    | 5.41 ms                                                             | 4.61 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                              | 280 ms: 1.17x faster                                                   |
| sqlite_synth            | 2.97 us                                                             | 2.59 us: 1.15x faster                                                  |
| sympy_sum               | 185 ms                                                              | 163 ms: 1.14x faster                                                   |
| meteor_contest          | 115 ms                                                              | 102 ms: 1.12x faster                                                   |
| xml_etree_parse         | 164 ms                                                              | 147 ms: 1.11x faster                                                   |
| pathlib                 | 19.8 ms                                                             | 17.8 ms: 1.11x faster                                                  |
| unpickle                | 15.0 us                                                             | 13.6 us: 1.10x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 102 ms: 1.10x faster                                                   |
| telco                   | 6.67 ms                                                             | 6.44 ms: 1.04x faster                                                  |
| mdp                     | 2.75 sec                                                            | 2.69 sec: 1.02x faster                                                 |
| regex_dna               | 213 ms                                                              | 209 ms: 1.02x faster                                                   |
| pidigits                | 190 ms                                                              | 189 ms: 1.00x faster                                                   |
| pickle                  | 10.2 us                                                             | 10.4 us: 1.01x slower                                                  |
| generators              | 75.7 ms                                                             | 77.7 ms: 1.03x slower                                                  |
| unpickle_list           | 4.94 us                                                             | 5.13 us: 1.04x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.12 ms: 1.06x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.55 ms: 1.10x slower                                                  |
| pickle_dict             | 27.8 us                                                             | 31.3 us: 1.13x slower                                                  |
| coverage                | 70.6 ms                                                             | 102 ms: 1.44x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.32x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: mypy
