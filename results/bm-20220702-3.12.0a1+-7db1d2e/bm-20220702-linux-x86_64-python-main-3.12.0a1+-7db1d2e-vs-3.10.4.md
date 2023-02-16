
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7db1d2e
- commit date: 2022-07-02
- overall geometric mean: 1.33x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.39 ms: 1.43x faster                                  |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.39x faster                                  |
| tornado_http   | 128 ms                                                 | 91.4 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 89.9 ms: 1.60x faster                                  |
| float          | 109 ms                                                 | 69.9 ms: 1.56x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 125 ms: 1.42x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| regex_dna      | 214 ms                                                 | 197 ms: 1.09x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.49 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 52.0 ms: 1.43x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.0 ms: 1.25x faster                                  |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                  |
| json_dumps           | 13.4 ms                                                | 11.9 ms: 1.13x faster                                  |
| pickle_list          | 4.72 us                                                | 4.28 us: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                   |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.22 ms: 1.71x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.07 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.55 ms: 1.53x faster                                  |
| django_template | 46.3 ms                                                | 32.0 ms: 1.44x faster                                  |
| Geometric mean  | (ref)                                                  | 1.49x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.27x faster                                  |
| logging_silent          | 176 ns                                                 | 91.7 ns: 1.92x faster                                  |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                   |
| pyflate                 | 676 ms                                                 | 389 ms: 1.74x faster                                   |
| go                      | 226 ms                                                 | 130 ms: 1.73x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 62.8 ms: 1.73x faster                                  |
| python_startup          | 14.1 ms                                                | 8.22 ms: 1.71x faster                                  |
| richards                | 75.2 ms                                                | 44.6 ms: 1.68x faster                                  |
| raytrace                | 467 ms                                                 | 282 ms: 1.65x faster                                   |
| chaos                   | 106 ms                                                 | 65.2 ms: 1.62x faster                                  |
| hexiom                  | 9.43 ms                                                | 5.88 ms: 1.60x faster                                  |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                   |
| nbody                   | 144 ms                                                 | 89.9 ms: 1.60x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 73.3 ms: 1.59x faster                                  |
| spectral_norm           | 150 ms                                                 | 94.3 ms: 1.59x faster                                  |
| float                   | 109 ms                                                 | 69.9 ms: 1.56x faster                                  |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.54x faster                                   |
| mako                    | 14.7 ms                                                | 9.55 ms: 1.53x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                   |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.44x faster                                  |
| chameleon               | 9.17 ms                                                | 6.39 ms: 1.43x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 52.0 ms: 1.43x faster                                  |
| regex_compile           | 177 ms                                                 | 125 ms: 1.42x faster                                   |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.42x faster                                 |
| logging_format          | 8.85 us                                                | 6.26 us: 1.41x faster                                  |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                  |
| tornado_http            | 128 ms                                                 | 91.4 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.39x faster                                  |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                   |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| fannkuch                | 488 ms                                                 | 373 ms: 1.31x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 45.5 ns: 1.31x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.21 ms: 1.29x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.0 ms: 1.25x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.2 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.24x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.1 ms: 1.20x faster                                  |
| sympy_expand            | 534 ms                                                 | 450 ms: 1.19x faster                                   |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                  |
| sympy_str               | 325 ms                                                 | 276 ms: 1.18x faster                                   |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                   |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                  |
| json_dumps              | 13.4 ms                                                | 11.9 ms: 1.13x faster                                  |
| meteor_contest          | 114 ms                                                 | 101 ms: 1.12x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| pickle_list             | 4.72 us                                                | 4.28 us: 1.10x faster                                  |
| regex_dna               | 214 ms                                                 | 197 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                   |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| telco                   | 6.73 ms                                                | 6.59 ms: 1.02x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.07 ms: 1.05x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.49 ms: 1.09x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
