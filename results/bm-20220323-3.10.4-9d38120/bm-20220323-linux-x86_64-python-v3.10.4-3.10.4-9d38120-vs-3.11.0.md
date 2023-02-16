
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.26x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 335 ms: 1.30x slower                                   |
| chameleon      | 6.41 ms                                                | 9.17 ms: 1.43x slower                                  |
| docutils       | 2.60 sec                                               | 3.18 sec: 1.22x slower                                 |
| html5lib       | 63.2 ms                                                | 85.9 ms: 1.36x slower                                  |
| tornado_http   | 96.6 ms                                                | 128 ms: 1.33x slower                                   |
| Geometric mean | (ref)                                                  | 1.33x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                   |
| float          | 76.3 ms                                                | 109 ms: 1.43x slower                                   |
| nbody          | 95.0 ms                                                | 144 ms: 1.51x slower                                   |
| Geometric mean | (ref)                                                  | 1.27x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.36 ms                                                | 3.19 ms: 1.05x faster                                  |
| regex_dna      | 203 ms                                                 | 214 ms: 1.05x slower                                   |
| regex_v8       | 22.3 ms                                                | 25.0 ms: 1.12x slower                                  |
| regex_compile  | 136 ms                                                 | 177 ms: 1.30x slower                                   |
| Geometric mean | (ref)                                                  | 1.10x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict          | 31.4 us                                                | 27.6 us: 1.14x faster                                  |
| unpickle_list        | 4.95 us                                                | 4.92 us: 1.01x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 163 ms: 1.03x slower                                   |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                  |
| json_dumps           | 12.7 ms                                                | 13.4 ms: 1.06x slower                                  |
| unpickle             | 13.3 us                                                | 14.2 us: 1.07x slower                                  |
| xml_etree_iterparse  | 103 ms                                                 | 111 ms: 1.08x slower                                   |
| json_loads           | 26.2 us                                                | 28.7 us: 1.09x slower                                  |
| pickle_list          | 4.17 us                                                | 4.72 us: 1.13x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 93.8 ms: 1.23x slower                                  |
| unpickle_pure_python | 225 us                                                 | 302 us: 1.34x slower                                   |
| xml_etree_process    | 53.8 ms                                                | 74.5 ms: 1.39x slower                                  |
| pickle_pure_python   | 304 us                                                 | 452 us: 1.49x slower                                   |
| Geometric mean       | (ref)                                                  | 1.13x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 5.78 ms: 1.03x faster                                  |
| python_startup         | 8.36 ms                                                | 14.1 ms: 1.69x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 63.7 ms: 1.22x slower                                  |
| genshi_text     | 22.1 ms                                                | 30.6 ms: 1.39x slower                                  |
| django_template | 32.5 ms                                                | 46.3 ms: 1.43x slower                                  |
| mako            | 9.85 ms                                                | 14.7 ms: 1.49x slower                                  |
| Geometric mean  | (ref)                                                  | 1.38x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| coverage                | 101 ms                                                 | 74.7 ms: 1.34x faster                                  |
| pickle_dict             | 31.4 us                                                | 27.6 us: 1.14x faster                                  |
| regex_effbot            | 3.36 ms                                                | 3.19 ms: 1.05x faster                                  |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                   |
| python_startup_no_site  | 5.96 ms                                                | 5.78 ms: 1.03x faster                                  |
| unpickle_list           | 4.95 us                                                | 4.92 us: 1.01x faster                                  |
| telco                   | 6.62 ms                                                | 6.73 ms: 1.02x slower                                  |
| xml_etree_parse         | 158 ms                                                 | 163 ms: 1.03x slower                                   |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                  |
| mdp                     | 2.62 sec                                               | 2.74 sec: 1.05x slower                                 |
| regex_dna               | 203 ms                                                 | 214 ms: 1.05x slower                                   |
| generators              | 72.2 ms                                                | 76.4 ms: 1.06x slower                                  |
| json_dumps              | 12.7 ms                                                | 13.4 ms: 1.06x slower                                  |
| unpickle                | 13.3 us                                                | 14.2 us: 1.07x slower                                  |
| json                    | 4.95 ms                                                | 5.35 ms: 1.08x slower                                  |
| xml_etree_iterparse     | 103 ms                                                 | 111 ms: 1.08x slower                                   |
| meteor_contest          | 105 ms                                                 | 114 ms: 1.09x slower                                   |
| json_loads              | 26.2 us                                                | 28.7 us: 1.09x slower                                  |
| pathlib                 | 18.2 ms                                                | 20.0 ms: 1.10x slower                                  |
| sympy_sum               | 166 ms                                                 | 183 ms: 1.11x slower                                   |
| regex_v8                | 22.3 ms                                                | 25.0 ms: 1.12x slower                                  |
| sympy_str               | 287 ms                                                 | 325 ms: 1.13x slower                                   |
| sympy_expand            | 472 ms                                                 | 534 ms: 1.13x slower                                   |
| pickle_list             | 4.17 us                                                | 4.72 us: 1.13x slower                                  |
| pylint                  | 463 ms                                                 | 532 ms: 1.15x slower                                   |
| sympy_integrate         | 20.9 ms                                                | 24.0 ms: 1.15x slower                                  |
| bench_thread_pool       | 810 us                                                 | 946 us: 1.17x slower                                   |
| flaskblogging           | 7.08 ms                                                | 8.27 ms: 1.17x slower                                  |
| sqlite_synth            | 2.49 us                                                | 2.92 us: 1.17x slower                                  |
| nqueens                 | 85.0 ms                                                | 100 ms: 1.18x slower                                   |
| dulwich_log             | 63.9 ms                                                | 75.8 ms: 1.19x slower                                  |
| async_generators        | 359 ms                                                 | 426 ms: 1.19x slower                                   |
| sqlalchemy_declarative  | 139 ms                                                 | 165 ms: 1.19x slower                                   |
| sqlalchemy_imperative   | 18.0 ms                                                | 21.5 ms: 1.19x slower                                  |
| coroutines              | 26.1 ms                                                | 31.6 ms: 1.21x slower                                  |
| docutils                | 2.60 sec                                               | 3.18 sec: 1.22x slower                                 |
| genshi_xml              | 52.1 ms                                                | 63.7 ms: 1.22x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 93.8 ms: 1.23x slower                                  |
| sqlglot_optimize        | 53.0 ms                                                | 65.2 ms: 1.23x slower                                  |
| scimark_sparse_mat_mult | 4.40 ms                                                | 5.45 ms: 1.24x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 134 ms: 1.25x slower                                   |
| fannkuch                | 388 ms                                                 | 488 ms: 1.26x slower                                   |
| async_tree_cpu_io_mixed | 752 ms                                                 | 949 ms: 1.26x slower                                   |
| gunicorn                | 1.12 ms                                                | 1.43 ms: 1.27x slower                                  |
| deepcopy                | 344 us                                                 | 438 us: 1.27x slower                                   |
| deepcopy_reduce         | 2.97 us                                                | 3.79 us: 1.28x slower                                  |
| scimark_fft             | 329 ms                                                 | 421 ms: 1.28x slower                                   |
| aiohttp                 | 1.05 ms                                                | 1.34 ms: 1.28x slower                                  |
| 2to3                    | 257 ms                                                 | 335 ms: 1.30x slower                                   |
| regex_compile           | 136 ms                                                 | 177 ms: 1.30x slower                                   |
| pycparser               | 1.17 sec                                               | 1.53 sec: 1.30x slower                                 |
| tornado_http            | 96.6 ms                                                | 128 ms: 1.33x slower                                   |
| logging_simple          | 6.06 us                                                | 8.10 us: 1.34x slower                                  |
| logging_format          | 6.62 us                                                | 8.85 us: 1.34x slower                                  |
| unpickle_pure_python    | 225 us                                                 | 302 us: 1.34x slower                                   |
| async_tree_none         | 529 ms                                                 | 711 ms: 1.34x slower                                   |
| html5lib                | 63.2 ms                                                | 85.9 ms: 1.36x slower                                  |
| async_tree_io           | 1.31 sec                                               | 1.78 sec: 1.36x slower                                 |
| unpack_sequence         | 43.4 ns                                                | 59.4 ns: 1.37x slower                                  |
| async_tree_memoization  | 625 ms                                                 | 855 ms: 1.37x slower                                   |
| pprint_pformat          | 1.44 sec                                               | 1.98 sec: 1.37x slower                                 |
| thrift                  | 752 us                                                 | 1.03 ms: 1.38x slower                                  |
| pprint_safe_repr        | 691 ms                                                 | 953 ms: 1.38x slower                                   |
| genshi_text             | 22.1 ms                                                | 30.6 ms: 1.39x slower                                  |
| xml_etree_process       | 53.8 ms                                                | 74.5 ms: 1.39x slower                                  |
| deepcopy_memo           | 36.4 us                                                | 51.7 us: 1.42x slower                                  |
| django_template         | 32.5 ms                                                | 46.3 ms: 1.43x slower                                  |
| float                   | 76.3 ms                                                | 109 ms: 1.43x slower                                   |
| chameleon               | 6.41 ms                                                | 9.17 ms: 1.43x slower                                  |
| sqlglot_transpile       | 1.66 ms                                                | 2.43 ms: 1.46x slower                                  |
| hexiom                  | 6.35 ms                                                | 9.43 ms: 1.48x slower                                  |
| mako                    | 9.85 ms                                                | 14.7 ms: 1.49x slower                                  |
| pickle_pure_python      | 304 us                                                 | 452 us: 1.49x slower                                   |
| sqlglot_parse           | 1.37 ms                                                | 2.04 ms: 1.49x slower                                  |
| scimark_lu              | 107 ms                                                 | 161 ms: 1.50x slower                                   |
| spectral_norm           | 99.9 ms                                                | 150 ms: 1.50x slower                                   |
| nbody                   | 95.0 ms                                                | 144 ms: 1.51x slower                                   |
| chaos                   | 68.6 ms                                                | 106 ms: 1.54x slower                                   |
| go                      | 143 ms                                                 | 226 ms: 1.57x slower                                   |
| crypto_pyaes            | 73.9 ms                                                | 117 ms: 1.58x slower                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 109 ms: 1.59x slower                                   |
| raytrace                | 290 ms                                                 | 467 ms: 1.61x slower                                   |
| pyflate                 | 417 ms                                                 | 676 ms: 1.62x slower                                   |
| richards                | 46.2 ms                                                | 75.2 ms: 1.63x slower                                  |
| python_startup          | 8.36 ms                                                | 14.1 ms: 1.69x slower                                  |
| scimark_sor             | 115 ms                                                 | 197 ms: 1.71x slower                                   |
| logging_silent          | 98.5 ns                                                | 176 ns: 1.79x slower                                   |
| deltablue               | 3.64 ms                                                | 7.28 ms: 2.00x slower                                  |
| Geometric mean          | (ref)                                                  | 1.26x slower                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
