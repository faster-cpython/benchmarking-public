
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 733e15f
- commit date: 2022-06-11
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                   |
| chameleon      | 9.17 ms                                                | 6.40 ms: 1.43x faster                                  |
| html5lib       | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| tornado_http   | 128 ms                                                 | 91.3 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 91.3 ms: 1.58x faster                                  |
| float          | 109 ms                                                 | 71.0 ms: 1.53x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| regex_dna      | 214 ms                                                 | 198 ms: 1.08x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.01 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.55x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 52.1 ms: 1.43x faster                                  |
| unpickle_pure_python | 302 us                                                 | 212 us: 1.42x faster                                   |
| xml_etree_generate   | 93.8 ms                                                | 75.4 ms: 1.24x faster                                  |
| pickle_list          | 4.72 us                                                | 4.11 us: 1.15x faster                                  |
| json_loads           | 28.7 us                                                | 25.1 us: 1.14x faster                                  |
| json_dumps           | 13.4 ms                                                | 12.0 ms: 1.12x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.06x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.02x faster                                   |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.26 ms: 1.71x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.11 ms: 1.06x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.74 ms: 1.50x faster                                  |
| django_template | 46.3 ms                                                | 31.2 ms: 1.48x faster                                  |
| Geometric mean  | (ref)                                                  | 1.49x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.51 ms: 2.07x faster                                  |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                   |
| logging_silent          | 176 ns                                                 | 99.2 ns: 1.78x faster                                  |
| richards                | 75.2 ms                                                | 43.6 ms: 1.73x faster                                  |
| go                      | 226 ms                                                 | 131 ms: 1.72x faster                                   |
| python_startup          | 14.1 ms                                                | 8.26 ms: 1.71x faster                                  |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                   |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.7 ms: 1.63x faster                                  |
| scimark_lu              | 161 ms                                                 | 102 ms: 1.58x faster                                   |
| nbody                   | 144 ms                                                 | 91.3 ms: 1.58x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.0 ms: 1.58x faster                                  |
| spectral_norm           | 150 ms                                                 | 95.3 ms: 1.57x faster                                  |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.55x faster                                  |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.55x faster                                   |
| float                   | 109 ms                                                 | 71.0 ms: 1.53x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.17 ms: 1.53x faster                                  |
| mako                    | 14.7 ms                                                | 9.74 ms: 1.50x faster                                  |
| django_template         | 46.3 ms                                                | 31.2 ms: 1.48x faster                                  |
| pycparser               | 1.53 sec                                               | 1.07 sec: 1.43x faster                                 |
| chameleon               | 9.17 ms                                                | 6.40 ms: 1.43x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 52.1 ms: 1.43x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 212 us: 1.42x faster                                   |
| tornado_http            | 128 ms                                                 | 91.3 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                   |
| logging_format          | 8.85 us                                                | 6.36 us: 1.39x faster                                  |
| logging_simple          | 8.10 us                                                | 5.84 us: 1.39x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 43.6 ns: 1.36x faster                                  |
| html5lib                | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                   |
| scimark_fft             | 421 ms                                                 | 315 ms: 1.34x faster                                   |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                   |
| fannkuch                | 488 ms                                                 | 382 ms: 1.28x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.36 ms: 1.25x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.4 ms: 1.24x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.9 ms: 1.22x faster                                  |
| nqueens                 | 100 ms                                                 | 83.4 ms: 1.20x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.50 us: 1.17x faster                                  |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                   |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                   |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                   |
| pickle_list             | 4.72 us                                                | 4.11 us: 1.15x faster                                  |
| json_loads              | 28.7 us                                                | 25.1 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.12x faster                                   |
| json                    | 5.35 ms                                                | 4.78 ms: 1.12x faster                                  |
| json_dumps              | 13.4 ms                                                | 12.0 ms: 1.12x faster                                  |
| regex_dna               | 214 ms                                                 | 198 ms: 1.08x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.06x faster                                   |
| regex_effbot            | 3.19 ms                                                | 3.01 ms: 1.06x faster                                  |
| telco                   | 6.73 ms                                                | 6.46 ms: 1.04x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.02x faster                                   |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| python_startup_no_site  | 5.78 ms                                                | 6.11 ms: 1.06x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
