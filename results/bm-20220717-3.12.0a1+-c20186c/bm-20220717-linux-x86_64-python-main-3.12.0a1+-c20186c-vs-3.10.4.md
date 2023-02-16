
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c20186c
- commit date: 2022-07-17
- overall geometric mean: 1.33x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.28 ms: 1.46x faster                                  |
| html5lib       | 85.9 ms                                                | 62.8 ms: 1.37x faster                                  |
| tornado_http   | 128 ms                                                 | 91.3 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 88.8 ms: 1.62x faster                                  |
| float          | 109 ms                                                 | 72.0 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| regex_dna      | 214 ms                                                 | 197 ms: 1.09x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.47 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                   |
| unpickle_pure_python | 302 us                                                 | 202 us: 1.50x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 52.2 ms: 1.43x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.2 ms: 1.25x faster                                  |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                  |
| json_dumps           | 13.4 ms                                                | 11.9 ms: 1.13x faster                                  |
| pickle_list          | 4.72 us                                                | 4.24 us: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| pickle               | 10.2 us                                                | 10.3 us: 1.02x slower                                  |
| unpickle_list        | 4.92 us                                                | 5.08 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.17 ms: 1.72x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.02 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.33 ms: 1.57x faster                                  |
| django_template | 46.3 ms                                                | 32.1 ms: 1.44x faster                                  |
| Geometric mean  | (ref)                                                  | 1.51x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.26x faster                                  |
| logging_silent          | 176 ns                                                 | 91.9 ns: 1.92x faster                                  |
| python_startup          | 14.1 ms                                                | 8.17 ms: 1.72x faster                                  |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                   |
| pyflate                 | 676 ms                                                 | 401 ms: 1.68x faster                                   |
| richards                | 75.2 ms                                                | 44.7 ms: 1.68x faster                                  |
| scimark_sor             | 197 ms                                                 | 117 ms: 1.68x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.1 ms: 1.67x faster                                  |
| raytrace                | 467 ms                                                 | 285 ms: 1.64x faster                                   |
| nbody                   | 144 ms                                                 | 88.8 ms: 1.62x faster                                  |
| spectral_norm           | 150 ms                                                 | 93.4 ms: 1.60x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 72.9 ms: 1.60x faster                                  |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                  |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                   |
| mako                    | 14.7 ms                                                | 9.33 ms: 1.57x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.05 ms: 1.56x faster                                  |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.53x faster                                   |
| float                   | 109 ms                                                 | 72.0 ms: 1.51x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 202 us: 1.50x faster                                   |
| chameleon               | 9.17 ms                                                | 6.28 ms: 1.46x faster                                  |
| pycparser               | 1.53 sec                                               | 1.05 sec: 1.46x faster                                 |
| logging_simple          | 8.10 us                                                | 5.61 us: 1.44x faster                                  |
| django_template         | 46.3 ms                                                | 32.1 ms: 1.44x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 52.2 ms: 1.43x faster                                  |
| logging_format          | 8.85 us                                                | 6.22 us: 1.42x faster                                  |
| tornado_http            | 128 ms                                                 | 91.3 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                   |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 43.2 ns: 1.37x faster                                  |
| html5lib                | 85.9 ms                                                | 62.8 ms: 1.37x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                  |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.34x faster                                   |
| fannkuch                | 488 ms                                                 | 373 ms: 1.31x faster                                   |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.2 ms: 1.25x faster                                  |
| dulwich_log             | 75.8 ms                                                | 60.8 ms: 1.25x faster                                  |
| regex_v8                | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.1 ms: 1.20x faster                                  |
| sympy_expand            | 534 ms                                                 | 452 ms: 1.18x faster                                   |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                  |
| sympy_str               | 325 ms                                                 | 278 ms: 1.17x faster                                   |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                  |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                   |
| json_dumps              | 13.4 ms                                                | 11.9 ms: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                  |
| meteor_contest          | 114 ms                                                 | 101 ms: 1.12x faster                                   |
| pickle_list             | 4.72 us                                                | 4.24 us: 1.11x faster                                  |
| regex_dna               | 214 ms                                                 | 197 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.04x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| pickle                  | 10.2 us                                                | 10.3 us: 1.02x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.08 us: 1.03x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.02 ms: 1.04x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.47 ms: 1.09x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
