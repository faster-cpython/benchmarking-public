
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: dec1ab0
- commit date: 2023-02-07
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 254 ms: 1.31x faster                                   |
| chameleon      | 8.86 ms                                                | 6.27 ms: 1.41x faster                                  |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.8 ms                                                | 60.8 ms: 1.41x faster                                  |
| tornado_http   | 128 ms                                                 | 94.6 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 108 ms                                                 | 72.1 ms: 1.49x faster                                  |
| nbody          | 136 ms                                                 | 95.4 ms: 1.43x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                   |
| regex_effbot   | 3.21 ms                                                | 3.44 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 286 us: 1.59x faster                                   |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.41 ms: 1.43x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                  |
| xml_etree_generate   | 93.3 ms                                                | 77.3 ms: 1.21x faster                                  |
| json_loads           | 28.9 us                                                | 24.1 us: 1.20x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| unpickle             | 14.3 us                                                | 13.0 us: 1.09x faster                                  |
| pickle_list          | 4.50 us                                                | 4.16 us: 1.08x faster                                  |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                   |
| pickle               | 10.1 us                                                | 10.1 us: 1.01x faster                                  |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                  |
| pickle_dict          | 28.3 us                                                | 31.2 us: 1.10x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.97 ms: 1.55x faster                                  |
| python_startup_no_site | 5.76 ms                                                | 6.49 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| mako            | 14.3 ms                                                | 9.72 ms: 1.47x faster                                  |
| django_template | 46.3 ms                                                | 33.5 ms: 1.38x faster                                  |
| genshi_xml      | 63.6 ms                                                | 46.7 ms: 1.36x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.30 ms: 2.24x faster                                  |
| logging_silent          | 173 ns                                                 | 93.8 ns: 1.85x faster                                  |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                   |
| richards                | 71.4 ms                                                | 41.8 ms: 1.71x faster                                  |
| pyflate                 | 675 ms                                                 | 399 ms: 1.69x faster                                   |
| go                      | 226 ms                                                 | 138 ms: 1.65x faster                                   |
| raytrace                | 461 ms                                                 | 287 ms: 1.61x faster                                   |
| chaos                   | 104 ms                                                 | 65.5 ms: 1.59x faster                                  |
| pickle_pure_python      | 453 us                                                 | 286 us: 1.59x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.58x faster                                  |
| hexiom                  | 9.42 ms                                                | 5.99 ms: 1.57x faster                                  |
| python_startup          | 13.9 ms                                                | 8.97 ms: 1.55x faster                                  |
| scimark_monte_carlo     | 105 ms                                                 | 68.1 ms: 1.54x faster                                  |
| spectral_norm           | 148 ms                                                 | 96.5 ms: 1.53x faster                                  |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                   |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| float                   | 108 ms                                                 | 72.1 ms: 1.49x faster                                  |
| mako                    | 14.3 ms                                                | 9.72 ms: 1.47x faster                                  |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.46x faster                                   |
| deepcopy_memo           | 50.0 us                                                | 34.2 us: 1.46x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.41 ms: 1.43x faster                                  |
| nbody                   | 136 ms                                                 | 95.4 ms: 1.43x faster                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.42x faster                                  |
| chameleon               | 8.86 ms                                                | 6.27 ms: 1.41x faster                                  |
| html5lib                | 85.8 ms                                                | 60.8 ms: 1.41x faster                                  |
| logging_format          | 8.92 us                                                | 6.39 us: 1.40x faster                                  |
| pprint_pformat          | 1.97 sec                                               | 1.42 sec: 1.39x faster                                 |
| logging_simple          | 8.06 us                                                | 5.78 us: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                  |
| django_template         | 46.3 ms                                                | 33.5 ms: 1.38x faster                                  |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.01 ms: 1.37x faster                                  |
| genshi_xml              | 63.6 ms                                                | 46.7 ms: 1.36x faster                                  |
| tornado_http            | 128 ms                                                 | 94.6 ms: 1.36x faster                                  |
| pprint_safe_repr        | 943 ms                                                 | 695 ms: 1.36x faster                                   |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.35x faster                                   |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                   |
| scimark_fft             | 414 ms                                                 | 308 ms: 1.34x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                 |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                  |
| unpack_sequence         | 59.5 ns                                                | 44.7 ns: 1.33x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                  |
| thrift                  | 1.03 ms                                                | 777 us: 1.33x faster                                   |
| fannkuch                | 477 ms                                                 | 362 ms: 1.32x faster                                   |
| deepcopy                | 429 us                                                 | 327 us: 1.31x faster                                   |
| 2to3                    | 332 ms                                                 | 254 ms: 1.31x faster                                   |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                 |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 665 ms: 1.28x faster                                   |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| deepcopy_reduce         | 3.75 us                                                | 2.97 us: 1.26x faster                                  |
| nqueens                 | 99.3 ms                                                | 78.8 ms: 1.26x faster                                  |
| coroutines              | 31.7 ms                                                | 25.2 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                   |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                  |
| bench_thread_pool       | 943 us                                                 | 781 us: 1.21x faster                                   |
| xml_etree_generate      | 93.3 ms                                                | 77.3 ms: 1.21x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                   |
| async_generators        | 428 ms                                                 | 356 ms: 1.20x faster                                   |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                   |
| json_loads              | 28.9 us                                                | 24.1 us: 1.20x faster                                  |
| dulwich_log             | 75.5 ms                                                | 63.1 ms: 1.20x faster                                  |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                   |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                   |
| sqlalchemy_imperative   | 21.0 ms                                                | 18.1 ms: 1.17x faster                                  |
| json                    | 5.35 ms                                                | 4.62 ms: 1.16x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| unpickle                | 14.3 us                                                | 13.0 us: 1.09x faster                                  |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                   |
| pickle_list             | 4.50 us                                                | 4.16 us: 1.08x faster                                  |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                   |
| telco                   | 6.68 ms                                                | 6.38 ms: 1.05x faster                                  |
| mdp                     | 2.82 sec                                               | 2.73 sec: 1.03x faster                                 |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                   |
| pickle                  | 10.1 us                                                | 10.1 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                  |
| generators              | 75.8 ms                                                | 76.8 ms: 1.01x slower                                  |
| regex_effbot            | 3.21 ms                                                | 3.44 ms: 1.07x slower                                  |
| pickle_dict             | 28.3 us                                                | 31.2 us: 1.10x slower                                  |
| python_startup_no_site  | 5.76 ms                                                | 6.49 ms: 1.13x slower                                  |
| coverage                | 75.3 ms                                                | 95.3 ms: 1.27x slower                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (6) of /home/mdboom/Work/builds/benchmarking/results/bm-20230207-3.12.0a4+-dec1ab0/bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
