
# Results vs. 3.10.4

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 258 ms: 1.29x faster                                   |
| chameleon      | 8.86 ms                                                | 6.63 ms: 1.34x faster                                  |
| docutils       | 3.18 sec                                               | 2.57 sec: 1.24x faster                                 |
| html5lib       | 85.8 ms                                                | 63.4 ms: 1.35x faster                                  |
| tornado_http   | 128 ms                                                 | 99.8 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 136 ms                                                 | 95.4 ms: 1.43x faster                                  |
| float          | 108 ms                                                 | 76.0 ms: 1.42x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 137 ms: 1.27x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                   |
| regex_effbot   | 3.21 ms                                                | 3.31 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 310 us: 1.46x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| unpickle_pure_python | 297 us                                                 | 229 us: 1.30x faster                                   |
| xml_etree_generate   | 93.3 ms                                                | 76.6 ms: 1.22x faster                                  |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.50 us                                                | 4.17 us: 1.08x faster                                  |
| json_dumps           | 13.5 ms                                                | 12.6 ms: 1.07x faster                                  |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                   |
| unpickle             | 14.3 us                                                | 13.4 us: 1.07x faster                                  |
| pickle               | 10.1 us                                                | 9.72 us: 1.04x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.04x faster                                   |
| unpickle_list        | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| pickle_dict          | 28.3 us                                                | 31.1 us: 1.10x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.49 ms: 1.64x faster                                  |
| python_startup_no_site | 5.76 ms                                                | 5.98 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.92 ms: 1.44x faster                                  |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                  |
| genshi_text     | 30.6 ms                                                | 22.1 ms: 1.38x faster                                  |
| genshi_xml      | 63.6 ms                                                | 52.5 ms: 1.21x faster                                  |
| Geometric mean  | (ref)                                                  | 1.35x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.67 ms: 2.02x faster                                  |
| logging_silent          | 173 ns                                                 | 102 ns: 1.70x faster                                   |
| scimark_sor             | 193 ms                                                 | 116 ms: 1.67x faster                                   |
| python_startup          | 13.9 ms                                                | 8.49 ms: 1.64x faster                                  |
| pyflate                 | 675 ms                                                 | 415 ms: 1.63x faster                                   |
| go                      | 226 ms                                                 | 140 ms: 1.62x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.62x faster                                  |
| raytrace                | 461 ms                                                 | 294 ms: 1.57x faster                                   |
| scimark_monte_carlo     | 105 ms                                                 | 68.4 ms: 1.53x faster                                  |
| richards                | 71.4 ms                                                | 46.9 ms: 1.52x faster                                  |
| chaos                   | 104 ms                                                 | 69.6 ms: 1.49x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.38 ms: 1.48x faster                                  |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.47x faster                                   |
| pickle_pure_python      | 453 us                                                 | 310 us: 1.46x faster                                   |
| spectral_norm           | 148 ms                                                 | 101 ms: 1.46x faster                                   |
| hexiom                  | 9.42 ms                                                | 6.46 ms: 1.46x faster                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.68 ms: 1.44x faster                                  |
| mako                    | 14.3 ms                                                | 9.92 ms: 1.44x faster                                  |
| nbody                   | 136 ms                                                 | 95.4 ms: 1.43x faster                                  |
| float                   | 108 ms                                                 | 76.0 ms: 1.42x faster                                  |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| genshi_text             | 30.6 ms                                                | 22.1 ms: 1.38x faster                                  |
| pprint_pformat          | 1.97 sec                                               | 1.44 sec: 1.37x faster                                 |
| logging_format          | 8.92 us                                                | 6.54 us: 1.36x faster                                  |
| async_tree_none         | 713 ms                                                 | 523 ms: 1.36x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 627 ms: 1.36x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                 |
| logging_simple          | 8.06 us                                                | 5.95 us: 1.35x faster                                  |
| html5lib                | 85.8 ms                                                | 63.4 ms: 1.35x faster                                  |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                   |
| pprint_safe_repr        | 943 ms                                                 | 700 ms: 1.35x faster                                   |
| deepcopy_memo           | 50.0 us                                                | 37.2 us: 1.34x faster                                  |
| chameleon               | 8.86 ms                                                | 6.63 ms: 1.34x faster                                  |
| unpack_sequence         | 59.5 ns                                                | 44.6 ns: 1.33x faster                                  |
| pycparser               | 1.51 sec                                               | 1.16 sec: 1.30x faster                                 |
| unpickle_pure_python    | 297 us                                                 | 229 us: 1.30x faster                                   |
| 2to3                    | 332 ms                                                 | 258 ms: 1.29x faster                                   |
| tornado_http            | 128 ms                                                 | 99.8 ms: 1.29x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 742 ms: 1.28x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.05 ms: 1.27x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.13 ms: 1.27x faster                                  |
| regex_compile           | 174 ms                                                 | 137 ms: 1.27x faster                                   |
| scimark_fft             | 414 ms                                                 | 327 ms: 1.26x faster                                   |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.25x faster                                   |
| fannkuch                | 477 ms                                                 | 384 ms: 1.24x faster                                   |
| docutils                | 3.18 sec                                               | 2.57 sec: 1.24x faster                                 |
| deepcopy                | 429 us                                                 | 349 us: 1.23x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 53.3 ms: 1.23x faster                                  |
| xml_etree_generate      | 93.3 ms                                                | 76.6 ms: 1.22x faster                                  |
| deepcopy_reduce         | 3.75 us                                                | 3.09 us: 1.21x faster                                  |
| genshi_xml              | 63.6 ms                                                | 52.5 ms: 1.21x faster                                  |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                  |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.59 ms: 1.20x faster                                  |
| async_generators        | 428 ms                                                 | 358 ms: 1.19x faster                                   |
| dulwich_log             | 75.5 ms                                                | 63.5 ms: 1.19x faster                                  |
| flaskblogging           | 8.38 ms                                                | 7.07 ms: 1.19x faster                                  |
| sqlite_synth            | 2.90 us                                                | 2.47 us: 1.18x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 141 ms: 1.17x faster                                   |
| sqlalchemy_imperative   | 21.0 ms                                                | 18.0 ms: 1.17x faster                                  |
| nqueens                 | 99.3 ms                                                | 85.0 ms: 1.17x faster                                  |
| bench_thread_pool       | 943 us                                                 | 813 us: 1.16x faster                                   |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                  |
| sympy_integrate         | 23.9 ms                                                | 21.0 ms: 1.14x faster                                  |
| sympy_expand            | 537 ms                                                 | 472 ms: 1.14x faster                                   |
| pylint                  | 519 ms                                                 | 461 ms: 1.13x faster                                   |
| sympy_str               | 324 ms                                                 | 289 ms: 1.12x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                  |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                   |
| pickle_list             | 4.50 us                                                | 4.17 us: 1.08x faster                                  |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                   |
| mdp                     | 2.82 sec                                               | 2.64 sec: 1.07x faster                                 |
| json_dumps              | 13.5 ms                                                | 12.6 ms: 1.07x faster                                  |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                   |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                   |
| unpickle                | 14.3 us                                                | 13.4 us: 1.07x faster                                  |
| pickle                  | 10.1 us                                                | 9.72 us: 1.04x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.04x faster                                   |
| generators              | 75.8 ms                                                | 73.3 ms: 1.03x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| regex_effbot            | 3.21 ms                                                | 3.31 ms: 1.03x slower                                  |
| python_startup_no_site  | 5.76 ms                                                | 5.98 ms: 1.04x slower                                  |
| pickle_dict             | 28.3 us                                                | 31.1 us: 1.10x slower                                  |
| coverage                | 75.3 ms                                                | 104 ms: 1.38x slower                                   |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): telco, bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221206-3.11.1-a7a450f/bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
