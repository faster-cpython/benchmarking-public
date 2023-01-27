
# Results vs. 3.10.4

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: linux-x86_64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 250 ms: 1.33x faster                                                       |
| chameleon      | 8.86 ms                                                | 6.38 ms: 1.39x faster                                                      |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.8 ms: 1.50x faster                                                      |
| nbody          | 136 ms                                                 | 95.4 ms: 1.43x faster                                                      |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                                       |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                       |
| regex_effbot   | 3.21 ms                                                | 3.54 ms: 1.10x slower                                                      |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.43x faster                                                      |
| json_loads           | 28.9 us                                                | 24.0 us: 1.21x faster                                                      |
| pickle               | 10.1 us                                                | 10.0 us: 1.01x faster                                                      |
| pickle_dict          | 28.3 us                                                | 30.4 us: 1.07x slower                                                      |
| pickle_list          | 4.50 us                                                | 3.96 us: 1.14x faster                                                      |
| pickle_pure_python   | 453 us                                                 | 286 us: 1.58x faster                                                       |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                      |
| unpickle_pure_python | 297 us                                                 | 196 us: 1.52x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| xml_etree_generate   | 93.3 ms                                                | 78.3 ms: 1.19x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.90 ms: 1.57x faster                                                      |
| python_startup_no_site | 5.76 ms                                                | 6.44 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                      |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                      |
| genshi_xml      | 63.6 ms                                                | 47.3 ms: 1.34x faster                                                      |
| mako            | 14.3 ms                                                | 9.70 ms: 1.47x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 250 ms: 1.33x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                                       |
| async_generators        | 428 ms                                                 | 351 ms: 1.22x faster                                                       |
| async_tree_none         | 713 ms                                                 | 523 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 756 ms: 1.26x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.36x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 626 ms: 1.37x faster                                                       |
| chameleon               | 8.86 ms                                                | 6.38 ms: 1.39x faster                                                      |
| chaos                   | 104 ms                                                 | 64.0 ms: 1.63x faster                                                      |
| bench_thread_pool       | 943 us                                                 | 779 us: 1.21x faster                                                       |
| coroutines              | 31.7 ms                                                | 25.2 ms: 1.26x faster                                                      |
| coverage                | 75.3 ms                                                | 96.1 ms: 1.27x slower                                                      |
| crypto_pyaes            | 118 ms                                                 | 72.1 ms: 1.63x faster                                                      |
| deepcopy                | 429 us                                                 | 327 us: 1.31x faster                                                       |
| deepcopy_reduce         | 3.75 us                                                | 3.00 us: 1.25x faster                                                      |
| deepcopy_memo           | 50.0 us                                                | 34.3 us: 1.46x faster                                                      |
| deltablue               | 7.39 ms                                                | 3.22 ms: 2.29x faster                                                      |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                      |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| dulwich_log             | 75.5 ms                                                | 62.1 ms: 1.22x faster                                                      |
| fannkuch                | 477 ms                                                 | 367 ms: 1.30x faster                                                       |
| float                   | 108 ms                                                 | 71.8 ms: 1.50x faster                                                      |
| generators              | 75.8 ms                                                | 75.1 ms: 1.01x faster                                                      |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                      |
| genshi_xml              | 63.6 ms                                                | 47.3 ms: 1.34x faster                                                      |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                                      |
| hexiom                  | 9.42 ms                                                | 5.99 ms: 1.57x faster                                                      |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                      |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.43x faster                                                      |
| json_loads              | 28.9 us                                                | 24.0 us: 1.21x faster                                                      |
| logging_format          | 8.92 us                                                | 6.31 us: 1.42x faster                                                      |
| logging_silent          | 173 ns                                                 | 92.5 ns: 1.87x faster                                                      |
| logging_simple          | 8.06 us                                                | 5.71 us: 1.41x faster                                                      |
| mako                    | 14.3 ms                                                | 9.70 ms: 1.47x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                     |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                       |
| mypy                    | 1.01 sec                                               | 806 ms: 1.26x faster                                                       |
| nbody                   | 136 ms                                                 | 95.4 ms: 1.43x faster                                                      |
| nqueens                 | 99.3 ms                                                | 78.5 ms: 1.27x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                      |
| pickle                  | 10.1 us                                                | 10.0 us: 1.01x faster                                                      |
| pickle_dict             | 28.3 us                                                | 30.4 us: 1.07x slower                                                      |
| pickle_list             | 4.50 us                                                | 3.96 us: 1.14x faster                                                      |
| pickle_pure_python      | 453 us                                                 | 286 us: 1.58x faster                                                       |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| pprint_safe_repr        | 943 ms                                                 | 667 ms: 1.41x faster                                                       |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.45x faster                                                     |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.38x faster                                                     |
| pyflate                 | 675 ms                                                 | 399 ms: 1.69x faster                                                       |
| python_startup          | 13.9 ms                                                | 8.90 ms: 1.57x faster                                                      |
| python_startup_no_site  | 5.76 ms                                                | 6.44 ms: 1.12x slower                                                      |
| raytrace                | 461 ms                                                 | 284 ms: 1.62x faster                                                       |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                                       |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                       |
| regex_effbot            | 3.21 ms                                                | 3.54 ms: 1.10x slower                                                      |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.17x faster                                                      |
| richards                | 71.4 ms                                                | 41.7 ms: 1.71x faster                                                      |
| scimark_fft             | 414 ms                                                 | 308 ms: 1.34x faster                                                       |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.46x faster                                                       |
| scimark_monte_carlo     | 105 ms                                                 | 65.2 ms: 1.61x faster                                                      |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                                       |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.95 ms: 1.39x faster                                                      |
| spectral_norm           | 148 ms                                                 | 98.9 ms: 1.50x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.43x faster                                                      |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                       |
| sqlite_synth            | 2.90 us                                                | 2.61 us: 1.11x faster                                                      |
| sympy_expand            | 537 ms                                                 | 451 ms: 1.19x faster                                                       |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                                      |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                       |
| sympy_str               | 324 ms                                                 | 269 ms: 1.20x faster                                                       |
| telco                   | 6.68 ms                                                | 6.30 ms: 1.06x faster                                                      |
| thrift                  | 1.03 ms                                                | 746 us: 1.38x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                                      |
| unpack_sequence         | 59.5 ns                                                | 41.9 ns: 1.42x faster                                                      |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                      |
| unpickle_pure_python    | 297 us                                                 | 196 us: 1.52x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| xml_etree_generate      | 93.3 ms                                                | 78.3 ms: 1.19x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
