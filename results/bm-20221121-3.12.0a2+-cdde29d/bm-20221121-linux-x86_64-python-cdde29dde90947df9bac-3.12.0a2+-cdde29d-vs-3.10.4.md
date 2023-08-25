
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 244 ms: 1.38x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.31 ms: 1.44x faster                                                  |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.1 ms: 1.45x faster                                                  |
| tornado_http   | 127 ms                                                 | 92.8 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.7 ms: 1.51x faster                                                  |
| float          | 111 ms                                                 | 73.1 ms: 1.51x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 52.8 ms: 1.42x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.3 ms: 1.23x faster                                                  |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                                  |
| pickle_list          | 4.56 us                                                | 3.97 us: 1.15x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                                   |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.12 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.56 ms: 1.54x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.2 ms: 1.50x faster                                                  |
| django_template | 45.9 ms                                                | 32.1 ms: 1.43x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.17 ms: 2.34x faster                                                  |
| logging_silent          | 175 ns                                                 | 94.1 ns: 1.86x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                   |
| richards                | 74.9 ms                                                | 41.3 ms: 1.81x faster                                                  |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                   |
| pyflate                 | 673 ms                                                 | 397 ms: 1.69x faster                                                   |
| python_startup          | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 65.0 ms: 1.67x faster                                                  |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                                   |
| chaos                   | 106 ms                                                 | 65.6 ms: 1.62x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 75.1 ms: 1.58x faster                                                  |
| spectral_norm           | 150 ms                                                 | 95.6 ms: 1.57x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.32 ms: 1.55x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 33.8 us: 1.55x faster                                                  |
| mako                    | 14.8 ms                                                | 9.56 ms: 1.54x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.18 ms: 1.54x faster                                                  |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                                   |
| nbody                   | 142 ms                                                 | 93.7 ms: 1.51x faster                                                  |
| float                   | 111 ms                                                 | 73.1 ms: 1.51x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.2 ms: 1.50x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.1 ms: 1.45x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.31 ms: 1.44x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.62 us: 1.44x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 45.1 ns: 1.43x faster                                                  |
| django_template         | 45.9 ms                                                | 32.1 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 52.8 ms: 1.42x faster                                                  |
| logging_format          | 8.91 us                                                | 6.29 us: 1.42x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 676 ms: 1.41x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.07 sec: 1.41x faster                                                 |
| aiohttp                 | 1.38 ms                                                | 991 us: 1.40x faster                                                   |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 748 us: 1.38x faster                                                   |
| scimark_fft             | 424 ms                                                 | 307 ms: 1.38x faster                                                   |
| 2to3                    | 336 ms                                                 | 244 ms: 1.38x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 622 ms: 1.37x faster                                                   |
| tornado_http            | 127 ms                                                 | 92.8 ms: 1.37x faster                                                  |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                  |
| async_tree_none         | 717 ms                                                 | 530 ms: 1.35x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                 |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| fannkuch                | 486 ms                                                 | 373 ms: 1.30x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.2 ms: 1.30x faster                                                  |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                  |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                 |
| deepcopy_reduce         | 3.82 us                                                | 2.99 us: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 61.5 ms: 1.23x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.3 ms: 1.23x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 774 us: 1.22x faster                                                   |
| nqueens                 | 100 ms                                                 | 82.0 ms: 1.22x faster                                                  |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                                  |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| async_generators        | 425 ms                                                 | 358 ms: 1.19x faster                                                   |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                 | 280 ms: 1.17x faster                                                   |
| pickle_list             | 4.56 us                                                | 3.97 us: 1.15x faster                                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.14x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.13x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                                   |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                 |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                  |
| telco                   | 6.54 ms                                                | 6.44 ms: 1.02x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| generators              | 76.8 ms                                                | 77.7 ms: 1.01x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.12 ms: 1.05x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.13 us: 1.06x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.3 us: 1.15x slower                                                  |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.32x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x
